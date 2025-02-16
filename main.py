from collections import defaultdict
from base64 import b64encode
from ollama import Client
from openai import OpenAI
from tqdm import tqdm
from time import time
import argparse
import json
import httpx


# Parse args
parser = argparse.ArgumentParser(description="AI benchmark")
parser.add_argument("--runner", required=True, type=str, help="Your rig codename")
parser.add_argument("--models", required=True, type=str, help="Comma-separated list of models")
parser.add_argument("--allowlist", type=str, help="Comma-separated list of prompts ids to run")
parser.add_argument("--ollama", action="store_true", help="Use Ollama API for inference (default)")
parser.add_argument("--openai", action="store_true", help="Use OpenAI API for inference")
parser.add_argument("--url", type=str, help="Ollama url (ignores ssl cert)")
parser.add_argument("--user", type=str, help="Ollama url http user (ignores ssl cert)")
parser.add_argument("--pwd", type=str, help="Ollama url http pass (ignores ssl cert)")
args = parser.parse_args()

runner = args.runner
models = args.models.split(',')
allowlist = [int(num) for num in args.allowlist.split(',')] if args.allowlist else None

if args.openai:
    inference = OpenAI().chat
elif args.url:
    auth_header = f"Basic {b64encode(f'{args.user}:{args.pwd}'.encode()).decode()}"
    transport = httpx.HTTPTransport(verify=False)
    http_client = httpx.Client(transport=transport, headers={"Authorization": auth_header})

    client = Client(host=args.url)
    client._client._transport = transport
    client._client.headers["Authorization"] = auth_header
    inference = client.chat
else:
    inference = Client(host="http://127.0.0.1:11434").chat

if args.openai:
    runner = "oai"


# File storage
with open("in-prompts.json", "r") as file:
    tasks = list(enumerate(json.load(file)))

with open("out-results.json.log", "r") as file:
    done = defaultdict(set)

    for line in file:
        data = json.loads(line)

        if "result" in data and data.get("runner", None) == runner:
            done[data["model"]].add(data["task_id"])

log = open("out-results.json.log", "a")


# Inference
for i, model in enumerate(models):
    print(f"Model {model} ({i + 1}/{len(models)})")

    unsolved_tasks = [task for task in tasks if task[0] not in done[model] and (allowlist == None or task[0] in allowlist)]

    for task_id, prompt in tqdm(unsolved_tasks):
        entry = {"model": model, "task_id": task_id, "runner": runner}

        try:
            started = time()
            entry["result"] = inference(model=model, messages=[{"role": "user", "content": prompt}]).model_dump()
            entry["elapsed_time"] = time() - started
            
        except Exception as e:
            if "not found, try pulling it first" in str(e):
                break

            entry["error"] = str(e)

        log.write(json.dumps(entry, ensure_ascii=False) + "\n")
        log.flush()
