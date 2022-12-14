# for more infomation about stablediffusion,see
# https://huggingface.co/blog/stable_diffusion
# https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion_2

# create cuda environment: https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html#uninstall-cuda-software
# check cuda version: https://qiita.com/Soleiyu/items/2b379da52c56aaa68c0c
# install pytorch: https://pytorch.org/get-started/locally/
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
import torch
import base64
import pickle
from io import BytesIO


def pil_to_base64(img, format="jpeg"):
    buffer = BytesIO()
    img.save(buffer, format)
    img_str = base64.b64encode(buffer.getvalue()).decode("ascii")

    return img_str

def img_gen(prompts: list[str]) -> list[str]:
    TOKEN = "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"

    # repo_id = "stabilityai/stable-diffusion-2-base"
    # pipe = DiffusionPipeline.from_pretrained(repo_id, torch_dtype=torch.float16, revision="fp16")
    # f = open("pipe.txt","wb")
    # pickle.dump(pipe, f)
    with open("pipe.txt", 'rb') as f:
        pipe = pickle.load(f)
    
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    # https://github-com.translate.goog/pytorch/pytorch/issues/30664?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=op,sc
    pipe = pipe.to("cuda")

    images_str = []
    for prompt in prompts:
        image = pipe(prompt, num_inference_steps=10).images[0]
        image_str = pil_to_base64(image)
        images_str.append(image_str)
    return images_str
