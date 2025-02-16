from collections import defaultdict
from ollama import Client
# from openai import OpenAI
from tqdm import tqdm
from time import time
import json


runner = "m3-max"
models = ["deepseek-r1:70b", "llama3.3:70b", "dolphin-mixtral:8x7b", "qwen2.5:32b", "command-r:latest"]
inference = Client(host="http://127.0.0.1:11434").chat

# runner = "m1"
# models = ["deepseek-r1:1.5b", "llama3.2:1b"]
# inference = Client(host="http://127.0.0.1:11434").chat

# runner = "oai"
# models = ["gpt-4o", "o1"]
# inference = OpenAI().chat.completions.create


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

    unsolved_tasks = [task for task in tasks if task[0] not in done[model]]

    for task_id, prompt in tqdm(unsolved_tasks):
        entry = {"model": model, "task_id": task_id, "runner": runner}

        try:
            started = time()
            entry["result"] = inference(model=model, messages=[{"role": "user", "content": prompt}]).model_dump()
            entry["elapsed_time"] = time() - started
            
        except Exception as e:
            entry["error"] = str(e)

        log.write(json.dumps(entry, ensure_ascii=False) + "\n")
        log.flush()
