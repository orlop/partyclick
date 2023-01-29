import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
from io import BytesIO

def automatic_lambda_img2img():
    url = "http://155.248.202.177:7860"
    capture_filename="/home/partyclick/shared/snapshot.jpg"
    img2img_name="/home/partyclick/shared/img2img.jpg"


    encoded = base64.b64encode(open(capture_filename, "rb").read()) #change the directory and image name to suit your needs
    encodedString=str(encoded, encoding='utf-8')
    GoodEncoded='data:image/jpg;base64,' + encodedString


    payload = {
        "init_images": [
            GoodEncoded
        ],
        "prompt": "paw patrol character",
        "negative_prompt": "kitsch, ugly, oversaturated, grain, low-res, Deformed, blurry",
        "steps": 45,
        "width": 512,
        "height": 512,
        "sampler_index": "Euler a",
        "cfg_scale": 7,
        "denoising_strength": 0.65
    }

    payloadJson = json.dumps(payload)

    response = requests.post(url=f'{url}/sdapi/v1/img2img', data=payloadJson)

    r = response.json()

    if r.get("images") is None:
        print("Error, got this returned:")
        print(r)
    else:
        for i in r['images']:
            image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

            png_payload = {
                "image": "data:image/png;base64," + i
            }
            response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

            pnginfo = PngImagePlugin.PngInfo()
            pnginfo.add_text("parameters", response2.json().get("info"))
            image.save(img2img_name, pnginfo=pnginfo)
