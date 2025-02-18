# Best hardware for LLM inference

## Median chars per second, only models with 95%+ good answers

|                          | Phi-4 14B   | DeepSeek-R1 32B   | Qwen2.5 32B   | DeepSeek-R1 70B   | Llama 3.3 70B   | ChatGPT 4o   | o1-mini   |
|:-------------------------|:------------|:------------------|:--------------|:------------------|:----------------|:-------------|:----------|
| OpenAI API               |             |                   |               |                   |                 | 356          | 430       |
| RTX 4090 24GB, 3650€     | 418         | 185               | 200           |                   |                 |              |           |
| RTX 5090 32GB, 5600€     | 607         | 284               | 314           | 23*               |                 |              |           |
| Dual RTX 4090 24GB 6000€ | 411         | 170               | 194           | 91                | 95              |              |           |
| Mac M3 Max 128GB, 6250€  | 136         | 64                | 65            | 28                | 29              |              |           |
| RTX A6000 48GB 7550€     | 280         | 129               | 135           | 66                | 70              |              |           |
| Dual RTX 5090 32GB 8100€ | 579         | 234               | 253           | 129               | 136             |              |           |
| RTX 6000Ada 48GB 10 000€ | 343         | 151               | 166           | 78                | 79              |              |           |
| A100 SXM4 40GB 23 000€   | 405         | 185               | 201           |                   |                 |              |           |

*cpu inference

## Hardware leaders

rtx 4090 -> budget option, for 32b models, may be scaled to x2 for 70b models
rtx 5090 -> best raw power
a6000 -> best for fine-tuning because of error correction (but its fine to just rent)

## Model leaders

## Hardware price breakdown

### RTX 4090

2150€ RTX 4090 24GB https://www.monitor.rs/graficke-karte/MSI-GeForce-RTX-4090-SUPRIM-X-24G
600€ AMD Ryzen 9 7950X
400-800€ Motherboard
120€ RAM
120€ m2 ssd
100€ PSU
80€ case

3650€ total

### RTX 5090

3800€ https://www.monitor.rs/graficke-karte/MSI-GForce-RTX-5090-32GB-GAMING-TRIO-OC

### A6000

6000€ https://iponcomp.com/shop/product/pny-vcnrtxa6000-pb-quadro-rtx-a6000-48-gb-gddr6-pcie/1906968

# Contributing to a project

## Run tests on your hardware and submit them as a pull request

```
# Install requirements
python3 -m pip install -r requirements.txt

# Start ollama app (mac) or service (linux)

# Pull models (you are not required to pull all, but highly recommended)
ollama pull llama2-uncensored:7b  # 3.8 GB
ollama pull deepseek-r1:7b        # 4.7 GB
ollama pull qwen2.5:14b           # 9.0 GB
ollama pull phi4:14b              # 9.1 GB
ollama pull deepseek-r1:32b       # 19 GB
ollama pull qwen2.5:32b           # 19 GB
ollama pull command-r:latest      # 18 GB
ollama pull dolphin-mixtral:8x7b  # 26 GB
ollama pull deepseek-r1:70b       # 42 GB
ollama pull llama3.3:70b          # 42 GB

# Run tests
python3 main.py --runner [YOUR_RUNNER_CODENAME]

# Commit and push your results, use rebase if needed
```

## Score results

Go to https://tgr.rs/ai-score/ and send me a pull request with exported data

## Run tests on rented hardware

https://www.runpod.io/
https://vast.ai/

### Running vast ai instance (example)

```
cd ~/Desktop/monorepo/github/mac-ai-bench

python3.11 main.py --runner [runner] --ignoressl --url [api_url] --user vastai --pwd [password]

afplay ~/Downloads/mon.mp3

# ~/Library/Python/3.11/bin/vastai destroy instance 123
```

# Some useful info

```

Z1AW001KQAB/A
Apple M3 Max 128 GB
12 performance and 4 efficiency cores
40 gpu cores metal 3

https://browser.geekbench.com/v6/cpu/10235074  
https://browser.geekbench.com/v6/compute/3585512  
https://browser.geekbench.com/v6/compute/3585495  

NAME                             ID              SIZE      MODIFIED   
deepseek-r1:70b                  0c1615a8ca32    42 GB     4 days ago    
llama3.3:70b                     a6eb4748fd29    42 GB     4 days ago    
dolphin-mixtral:8x7b             4f76c28c0414    26 GB     4 days ago    
deepseek-r1:7b                   0a8c26691023    4.7 GB    4 days ago    
qwen2.5:14b                      7cdf5a0187d5    9.0 GB    4 days ago    
llama2-uncensored:7b             44040b922233    3.8 GB    4 days ago    
qwen2.5:32b                      9f13ba1299af    19 GB     4 days ago    
command-r:latest                 7d96360d357f    18 GB     4 days ago    
deepseek-r1:32b                  38056bbcbb2d    19 GB     4 days ago    
phi4:14b                         ac896e5b8b34    9.1 GB    4 days ago    
mxbai-embed-large:latest         468836162de7    669 MB    4 days ago    
llava-phi3:latest                c7edd7b87593    2.9 GB    4 days ago    
deepseek-r1:latest               0a8c26691023    4.7 GB    4 days ago    
llava-llama3:latest              44c161b1f465    5.5 GB    4 days ago    
phi3:latest                      4f2222927938    2.2 GB    4 days ago    
llama3.2-vision:latest           085a1fdae525    7.9 GB    4 days ago    
nomic-embed-text:latest          0a109f422b47    274 MB    4 days ago    
duckdb-nsql:latest               3ed734989690    3.8 GB    4 days ago    
gemma2:latest                    ff02c3702f32    5.4 GB    4 days ago    
tinyllama:latest                 2644915ede35    637 MB    4 days ago    
llama3.2:latest                  a80c4f17acd5    2.0 GB    4 days ago    
snowflake-arctic-embed:latest    21ab8b9b0545    669 MB    4 days ago    
qwq:latest                       46407beda5c0    19 GB     4 days ago    
gemma2:2b                        8ccf136fdd52    1.6 GB    4 days ago    
codegemma:latest                 0c96700aaada    5.0 GB    4 days ago    
llava:7b-v1.6                    8dd30f6b0cb1    4.7 GB    4 days ago    
granite-code:20b                 59db7b531bb4    11 GB     4 days ago    
granite3-dense:8b                199456d876ee    4.9 GB    4 days ago    
granite3-moe:latest              d84e1e38ee39    821 MB    4 days ago    
llama3.3:latest                  a6eb4748fd29    42 GB     4 days ago    
mistral-nemo:latest              994f3b8b7801    7.1 GB    4 days ago    
llama3.1:latest                  46e0c10c039e    4.9 GB    4 days ago    
mistral:latest                   f974a74358d6    4.1 GB    4 days ago    
wizardlm2:latest                 c9b1aff820f2    4.1 GB    4 days ago    
codestral:latest                 0898a8b286d5    12 GB     4 days ago    
starcoder2:3b                    9f4ae0aff61e    1.7 GB    4 days ago    
mistral-openorca:latest          12dc6acc14d0    4.1 GB    4 days ago    
codellama:python                 120ca3419eae    3.8 GB    4 days ago    
deepseek-coder-v2:latest         63fb193b3a9b    8.9 GB    4 days ago    
aya:latest                       7ef8c4942023    4.8 GB    4 days ago    
vicuna:latest                    370739dc897b    3.8 GB    4 days ago    
codellama:latest                 8fdf8f752f6e    3.8 GB    4 days ago    
deepseek-coder-v2:16b            63fb193b3a9b    8.9 GB    4 days ago    
llama3.1:70b                     711a9e8463af    42 GB     4 days ago    
llama3.2-vision:11b              085a1fdae525    7.9 GB    4 days ago    
llama3.2-vision:90b              d2a5e64c56a9    54 GB     4 days ago    
llama3.2:1b                      baf6a787fdff    1.3 GB    4 days ago    
llama3.2:3b                      a80c4f17acd5    2.0 GB    4 days ago    
llava-phi3:3.8b                  c7edd7b87593    2.9 GB    4 days ago    
llava-llama3:8b                  44c161b1f465    5.5 GB    4 days ago    
llava:13b                        0d0eb4d7f485    8.0 GB    4 days ago    
llava:7b                         8dd30f6b0cb1    4.7 GB    4 days ago    
mxbai-embed-large:335m           468836162de7    669 MB    4 days ago    
mistral:7b                       f974a74358d6    4.1 GB    4 days ago    
phi3:14b                         cf611a26b048    7.9 GB    4 days ago    
phi3:3.8b                        4f2222927938    2.2 GB    4 days ago    
qwen2.5-coder:14b                3028237cc8c5    9.0 GB    4 days ago    
qwen2.5-coder:32b                4bd6cbf2d094    19 GB     4 days ago
qwen2.5:0.5b                     a8b0c5157701    397 MB    4 days ago    
qwen2.5:1.5b                     65ec06548149    986 MB    4 days ago    
qwen2.5-coder:7b                 2b0496514337    4.7 GB    4 days ago    
qwen2.5:72b                      424bad2cc13f    47 GB     4 days ago    
qwen2.5:3b                       357c53fb659c    1.9 GB    4 days ago    
vicuna:13b                       e311d03837d9    7.4 GB    4 days ago    
qwen2.5:7b                       845dbda0ea48    4.7 GB    4 days ago    
vicuna:33b                       86f0704901a4    18 GB     4 days ago    
aya:35b                          bab44e009440    20 GB     4 days ago    
vicuna:7b                        370739dc897b    3.8 GB    4 days ago    
llama2-uncensored:70b            bdd0ec2f5ec5    38 GB     4 days ago    
mixtral:8x22b                    e8479ee1cb51    79 GB     4 days ago    
dolphincoder:15b                 1102380927c2    9.1 GB    4 days ago    
dolphin-mixtral:8x22b            0772a1b884bf    79 GB     4 days ago    
mixtral:8x7b                     a3b6bef0f836    26 GB     4 days ago    
dolphincoder:7b                  677555f1f316    4.2 GB    4 days ago    
qwen2.5:latest                   845dbda0ea48    4.7 GB    4 days ago    
llama2-uncensored:latest         44040b922233    3.8 GB    4 days ago    
qwen2.5-coder:latest             2b0496514337    4.7 GB    4 days ago    
llava:latest                     8dd30f6b0cb1    4.7 GB    4 days ago    
mixtral:latest                   a3b6bef0f836    26 GB     4 days ago    
phi4:latest                      ac896e5b8b34    9.1 GB    4 days ago    

RTX 4090 24GB
KMPG-D32 Series
AMD EPYC 7343 16-core

RTX 5090 32GB
X870 GAMING
AMD Ryzen 9 7950X 16-core

RTX A6000 48GB
Xeon® Gold 6248R

RTX 6000Ada 48GB
H12DSG-O-
AMD EPYC 7443 24-core

2x RTX 4090 24GB
ROME2D32GM-2T
AMD EPYC 7B13 64-core

2x RTX 5090 32GB
H13SSL-NT
AMD EPYC 9124 16-core

A100 SXM4 40GB
AMD EPYC 7543 32-core

RTX 5090 32GB
ROG STRIX X870-A GAMING WIFI
AMD Ryzen 9 9950X 16-core

RTX 5090 32GB
GENOA2D24G-2L
AMD EPYC 9654 96-core

```

# TODO/IDEAS:
- Evaluate also multimessage prompts (maybe chatgpt assisted dialogues)
- Evaluate using another AI (chatgpt)
- Rename ai-score to Arena
- Make ai-score data builder based on main.json.log
- Rewrite readme, put tables in it
- Write more tg posts about topic
- Measure rtx 4090 + cpu
