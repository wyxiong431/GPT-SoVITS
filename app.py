import subprocess

import os

from tqdm import tqdm





def run_commands(commands):

    for i, command in enumerate(tqdm(commands, desc="正在启动，进度...")):

        process = subprocess.Popen(command, shell=True)

        process.wait()



# @title Download pretrained models 下载预训练模型
#!mkdir -p /content/GPT-SoVITS/GPT_SoVITS/pretrained_models
#!mkdir -p /content/GPT-SoVITS/tools/damo_asr/models
#!mkdir -p /content/GPT-SoVITS/tools/uvr5
#%cd /content/GPT-SoVITS/GPT_SoVITS/pretrained_models
#!git clone https://huggingface.co/lj1995/GPT-SoVITS
#%cd /content/GPT-SoVITS/tools/damo_asr/models
#!git clone https://www.modelscope.cn/damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch.git
#!git clone https://www.modelscope.cn/damo/speech_fsmn_vad_zh-cn-16k-common-pytorch.git
#!git clone https://www.modelscope.cn/damo/punc_ct-transformer_zh-cn-common-vocab272727-pytorch.git
# @title UVR5 pretrains 安装uvr5模型
#%cd /content/GPT-SoVITS/tools/uvr5
#!git clone https://huggingface.co/Delik/uvr5_weights
#!git config core.sparseCheckout true
#!mv /content/GPT-SoVITS/GPT_SoVITS/pretrained_models/GPT-SoVITS/* /content/GPT-SoVITS/GPT_SoVITS/pretrained_models/
     

def start():

    commands = [

        f'echo 1. 正在下载前置模型... && !mkdir -p /content/GPT-SoVITS/GPT_SoVITS/pretrained_models,

        f'echo 2. 正在下载推理模型... && !mkdir -p /content/GPT-SoVITS/tools/damo_asr/models,

        f'echo 3. 正在下载 nltk 数据包... && !mkdir -p /content/GPT-SoVITS/tools/uvr5,

        f'echo 4. 正在解压前置模型 && %cd /content/GPT-SoVITS/GPT_SoVITS/pretrained_models,

        f'echo 5. 正在解压推理模型 && !git clone https://huggingface.co/lj1995/GPT-SoVITS,

        f'echo 6. 正在解压 nltk 数据包 && %cd /content/GPT-SoVITS/tools/damo_asr/models,
        f'echo 7. 正在解压 nltk1 数据包 && !git clone https://www.modelscope.cn/damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch.git,

        f'python -u GPT_SoVITS/inference_webui.py'

    ]

    run_commands(commands)



start()
