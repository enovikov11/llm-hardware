from collections import defaultdict
from base64 import b64encode
from ollama import Client
from openai import OpenAI
from tqdm import tqdm
from time import time
import argparse
import httpx
import json 
import os


parser = argparse.ArgumentParser(description="AI benchmark")
parser.add_argument("--runner", required=True, type=str, help="Your rig codename")
parser.add_argument("--models", type=str, help="Comma-separated list of models", default="phi4:14b,deepseek-r1:32b,qwen2.5:32b,deepseek-r1:70b,llama3.3:70b")
parser.add_argument("--prompts", type=str, help="main, all or comma-separated list of prompts ids", default="main")
parser.add_argument("--openai", action="store_true", help="Use OpenAI API for inference")
parser.add_argument("--url", type=str, help="Ollama URL")
parser.add_argument("--ignoressl", action="store_true", help="Ignore ssl cert (insecure)")
parser.add_argument("--user", type=str, help="HTTP user")
parser.add_argument("--pwd", type=str, help="HTTP password")
args = parser.parse_args()

runner = "oai" if args.openai else args.runner
models = args.models.split(",")
prompts_filter = args.prompts if args.prompts in ("main", "all") else [int(n) for n in args.prompts.split(",")]

if args.openai:
    inference = OpenAI().chat
elif args.url:
    auth_header = f"Basic {b64encode(f'{args.user}:{args.pwd}'.encode()).decode()}"
    transport = httpx.HTTPTransport(verify=not args.ignoressl)
    http_client = httpx.Client(transport=transport, headers={"Authorization": auth_header})

    client = Client(host=args.url)
    client._client._transport = transport
    client._client.headers["Authorization"] = auth_header
    inference = client.chat
else:
    inference = Client(host="http://127.0.0.1:11434").chat

done = defaultdict(set)
prompts = []

for file in os.listdir("."):
    if not file.endswith(".json.log"):
        continue

    with open(file, "r") as file:
        for line in file:
            item = json.loads(line)

            if item["type"] == "run" and "result" in item and item["runner"] == runner:
                done[item["model"]].add(item["prompt_id"])
            elif item["type"] == "prompt" and \
            (prompts_filter == "all" or (item.get("main") if prompts_filter == "main" else item["prompt_id"] in prompts_filter)):
                prompts.append(item)

log = open(f"{int(time())}.json.log", "a")

for i, model in enumerate(models):
    print(f"Model {model} ({i + 1}/{len(models)})")
    tasks = [prompt for prompt in prompts if prompt["prompt_id"] not in done[model]]

    for task in tqdm(tasks):
        entry = {"type": "run", "runner": runner, "model": model, "prompt_id": task["prompt_id"]}

        try:
            started = time()
            result = inference(model=model, messages=[{"role": "user", "content": task["prompt"]}]).model_dump()
            entry["elapsed_time"] = time() - started
            entry["result"] = result
            
        except Exception as e:
            if "not found, try pulling it first" in str(e):
                break

            entry["error"] = str(e)

        log.write(json.dumps(entry, ensure_ascii=False) + "\n")
        log.flush()

log.close()
