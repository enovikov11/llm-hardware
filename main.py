from collections import defaultdict
# from ollama import Client
from openai import OpenAI
from tqdm import tqdm
from time import time
import json

runner = None

# Config Ollama
# models = ["deepseek-r1:70b", "llama3.3:70b", "dolphin-mixtral:8x7b", "qwen2.5:32b", "command-r:latest"]
# client = Client(host="http://127.0.0.1:11434")
# query = lambda model, prompt: client.chat(model=model, messages=[{"role": "user", "content": prompt}]).model_dump()

# Config OAI
models = ["gpt-4o", "o1"]
client = OpenAI()
query = lambda model, prompt: client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}]).model_dump()

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
            entry["result"] = query(model, prompt)
            entry["elapsed_time"] = time() - started
            
        except Exception as e:
            entry["error"] = str(e)

        log.write(json.dumps(entry, ensure_ascii=False) + "\n")
        log.flush()
