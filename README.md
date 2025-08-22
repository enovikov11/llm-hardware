# Best hardware for LLM inference

Warning: This is some raw data and analytics, nor an ultimate nor complete guide. Use your own judjement and consume this with some grain of salt (this is good strategy not only in choosing llm inference hardware :) )

## TODO

- Add actual small and big distilled models: oss, kimi k2, qwen 3

## Strategies

- GPU-first RAM: runs medium 32b-70b models at chatgpt-like speed with kinda ok intelligence
- CPU-first RAM: runs biggest 761b models with chatgpt-like intelligence but x10 slower
- Unified RAM (Apple M-series): power efficient option for medium models x5 slower

### GPUs

- RTX 4090: budget option, for 32b models, may be scaled to x2 for 70b models
- RTX 5090: best raw power
- RTX a6000: best for fine-tuning because of error correction (but its fine to just rent)

Note: x16/x16 pci is available only on server grade motherboard+cpu (1500+ €)

## Median chars per second, only models with 95%+ good answers

|                          | Phi-4 14B   | DeepSeek-R1 32B   | Qwen2.5 32B   | DeepSeek-R1 70B   | Llama 3.3 70B   | ChatGPT 4o   | o1-mini   |
|:-------------------------|:------------|:------------------|:--------------|:------------------|:----------------|:-------------|:----------|
| OpenAI API               |             |                   |               |                   |                 | 356          | 430       |
| RTX 4090 24GB, 3400€     | 418         | 185               | 200           |                   |                 |              |           |
| RTX 5090 32GB, 5600€     | 607         | 284               | 314           | 23*               |                 |              |           |
| Dual RTX 4090 24GB 6000€ | 411         | 170               | 194           | 91                | 95              |              |           |
| Mac M3 Max 128GB, 6250€  | 136         | 64                | 65            | 28                | 29              |              |           |
| RTX A6000 48GB 7550€     | 280         | 129               | 135           | 66                | 70              |              |           |
| Dual RTX 5090 32GB 8100€ | 579         | 234               | 253           | 129               | 136             |              |           |
| RTX 6000Ada 48GB 10 000€ | 343         | 151               | 166           | 78                | 79              |              |           |
| A100 SXM4 40GB 23 000€   | 405         | 185               | 201           |                   |                 |              |           |
| RTX 4080 16GB            | 303         |                   |               |                   |                 |              |           |
| dual-rtx-3090            | 295         | 145               | 154           | 77                | 79*             |              |           |
| macstuido-m2-max-64g     | 138         | 62                | 69            | 31                | 32              |              |           |
| mefes-m1-16g             | 32          |                   |               |                   |                 |              |           |
| rtx-3090                 | 370         | 161               | 179           |                   |                 |              |           |
| rtx-4090-cpu             |             |                   |               | 5*                |                 |              |           |


*cpu inference

# Contributing to a project

## Run tests on your hardware and submit them as a pull request

```
# Install requirements
python3 -m pip install -r requirements.txt

# Start ollama app (mac) or service (linux)

# Pull models (you are not required to pull all, but highly recommended)
ollama pull phi4:14b              # 9.1 GB
ollama pull deepseek-r1:32b       # 19 GB
ollama pull qwen2.5:32b           # 19 GB

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

# TODO
- Test RTX3090 with nvlink
- Test EPYC 7702 CPU only

- Test dual non-ollama inference
- Evaluate also multimessage prompts (maybe chatgpt assisted dialogues)
- Evaluate using another AI (chatgpt)

# Ideas

- Make on-demand ollama and test its usage myself
- [no available] Test AMD XT 7900 XTX 24GB
- Write more tg posts about topic
- Rename ai-score to Arena
- Make ai-score data builder based on main.json.log

# Hardware component prices

## GPU

600€ RTX 3090 24GB (used) https://www.kupujemprodajem.com/pretraga?keywords=rtx%203090&locationId=1&priceFrom=500&priceTo=1000&currency=eur
2600€ RTX 4090 24GB
6000€ RTX A6000 https://iponcomp.com/shop/product/pny-vcnrtxa6000-pb-quadro-rtx-a6000-48-gb-gddr6-pcie/1906968

590€ AMD Ryzen 9 7950X https://iponcomp.com/shop/product/amd-ryzen-9-7950x-450ghz-am5-box-100-100000514wof/2066371
520€ ASUS ROG STRIX X670E-F GAMING WIFI https://iponcomp.com/shop/product/asus-rog-strix-x670e-f-gaming-wifi/2100303
250€ 32GB RAM https://iponcomp.com/shop/product/kingston-fury-32gb-beast-expo-ddr5-6000mhz-cl30-kit-kf560c30bbek2-32/2260467
180€ SSD SAMSUNG 2TB 990 PRO M.2 https://iponcomp.com/shop/product/samsung-2tb-990-pro-m2-pcie-m2-2280-mz-v9p2t0bw/2066316

rtx 3090 24GB https://www.amazon.com/ZOTAC-Graphics-IceStorm-Advanced-ZT-A30900J-10P/dp/B08ZL6XD9H/ref=sr_1_1
rtx 3090 24GB renewed nvlink https://www.amazon.com/MSI-3090-Architecture-3X-24G/dp/B094PSPVPC/ref=sr_1_3

1100 eur AMD XT 7900 XTX 24GB
2850 eur Radeon Pro W7800 32GB

## CPU

750 eur epyc 7702 used

https://iponcomp.com/shop/product/supermicro-x12spl-f-motherboard/2138052
8 x https://iponcomp.com/shop/product/crucial-64gb-ddr4-3200mhz-ecc-mta36asf8g72pz-3g2r/2070919
https://iponcomp.com/shop/product/intel-xeon-silver-4309y-280ghz-lga-4189-oem/2225485


https://iponcomp.com/shop/product/intel-xeon-silver-4310-210ghz-lga-4189-oem/2234947

https://iponcomp.com/shop/product/amd-epyc-7302p-280ghz-sp3-oem-100-000000049/1811779

PSU
Case
Cooling

# Unsorted

https://digitalspaceport.com/how-to-run-deepseek-r1-671b-fully-locally-on-2000-epyc-rig/

https://cloud.vast.ai/api/v0/bundles/?q={"rentable":{"eq":true},"num_gpus":{"gte":2,"lte":2},"gpu_name":{"in":["RTX 4090"]},"limit":1000}

nvidia-smi nvlink -s

4x rtx 3090 24gb

https://cloud.vast.ai/api/v0/bundles/?q={"show_incompatible":{"eq":true},"cpu_ram":{"gte":440871.89976053947,"lte":8388608},"gpu_name":{"in":["RTX 3090","H200","Titan V","Titan X","Titan Xp","Titan RTX","RTX 5090","RTX 5080","RTX 4090","RTX 4090D","RTX 4080S","RTX 4080","RTX 4070S Ti","RTX 4070S","RTX 4070 Ti","RTX 4070","RTX 4060 Ti","RTX 4060","RTX 3090 Ti","RTX 3080 Ti","RTX 3080","RTX 3070 Ti","RTX 3070","RTX 3070 laptop","RTX 3060 Ti","RTX 3060","RTX 3060 laptop","RTX 3050","RTX 2080 Ti","RTX 2080S","RTX 2080","RTX 2070S","RTX 2070","RTX 2060S","RTX 2060","RTX 6000Ada","RTX 5000Ada","RTX 4500Ada","RTX 4000Ada","RTX A6000","RTX A5000","RTX A4500","RTX A4000","RTX A2000","A100 PCIE","A800 PCIE","A100 SXM4","A100X","A100 SXM","GH200 SXM","H100 PCIE","H100 SXM","H100 NVL","A40","A30","A16","A10g","A10","L40S","L40","L4","Tesla K80","Tesla P100","Tesla P40","Tesla P4","Tesla V100","GTX 1660 Ti","GTX 1660 S","GTX 1660","GTX 1650 S","GTX 1650","GTX 1080 Ti","GTX 1080","GTX 1070 Ti","GTX 1070","GTX 1060 6GB","GTX 1050 Ti","GTX 1050","GTX 980 Ti","GTX 980","GTX 970","GTX 960","GTX 750 Ti","GTX 750","Q RTX 8000","Q RTX 6000","Q RTX 5000","Q RTX 4000","P104-100","P106-100","GP100","Quadro P6000","Quadro P5000","Quadro P4000","Quadro P2000"]},"num_gpus":{"gte":0,"lte":18}}

## Cooling

- fan (little to no maintenance)
- liquid (better for high power)
- immersive (oils corrupt and oxidizes, novec is expensive and experimental)

# Specs

## vast ai

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

1x RTX 3090 24GB
B550 AORUS ELITE v2
AMD Ryzen 7 5800X 8-core

2x RTX 3090 24GB
X10DRX
Xeon® E5-2699 v4

1x RTX 4090 24GB (cpu)
PRIME B550-PLUS
AMD Ryzen 5 2600X 6-core

## Apple M3 Max 128 GB
Z1AW001KQAB/A
12 performance and 4 efficiency cores
40 gpu cores metal 3

https://browser.geekbench.com/v6/cpu/10235074  
https://browser.geekbench.com/v6/compute/3585512  
https://browser.geekbench.com/v6/compute/3585495  

## virt5070TI

hyper specs:

MB: ASUS TUF GAMING B650-PLUS WIFI
CPU: AMD Ryzen 7 7800X3D 8-Core Processor
RAM: 64GB Kingston KF560C36-32 x2 - 64GB
GPU: Nvidia 5700 Ti 16GB

Računar GAME CENTAR Electron - AMD Ryzen 7 7800X3D/64GB/2TB/RTX 5070 Ti 16GB - 347.298 RSD (with PDV)

## Models downloaded on M3 Max

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