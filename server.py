#%%
import time
import torch
import base64
import logging
import configparser
from PIL import Image
from io import BytesIO
from pathlib import Path
from datetime import datetime
from ultralytics import YOLOv10
from flask import Flask, request, jsonify, jsonify

#%%
config = configparser.ConfigParser()
config.read(r'config.ini', encoding='utf-8')

weights = config['Model']['WEIGHTS']
confidence = float(config['Model']['CONF'])
img_size = int(config['Model']['IMGSZ'])
log_path = config['Model']['LOG']

Path(log_path).mkdir(parents=True, exist_ok=True)

logging.basicConfig(filename=Path(log_path) / f"{datetime.now().strftime('%Y-%m-%d')}.log", 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info(f"******************** Start ********************")
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLOv10(weights).to(device)
logging.info(f"Model loaded: {weights}")
logging.info(f"Device: {device}")
logging.info(f"Image size: {img_size}")
logging.info(f"Confidence: {confidence}")

#%%
app = Flask(__name__)

@app.route("/img", methods=['POST'])
def detect():
    messages, answer = '', ''
    logging.info('---------------------------------------------')
    try:
        get_info = request.get_json()
        img_b64 = get_info['IMG']
        img_bytes = base64.b64decode(img_b64)
        img = Image.open(BytesIO(img_bytes)).convert('RGB')

        s = time.time()
        with torch.no_grad(): #不追蹤Tensor的梯度計算，減少記憶體使用量
            results = model(img, imgsz=img_size, conf=confidence)
        logging.info(f"{img} inference is finished, time: {time.time()-s:.2f}s")

        if len(results[0].boxes.cls) == 0:
            answer = ''
            messages = 'Success! No objects detected.'
        else:
            cls = results[0].boxes.cls.detach().cpu().numpy()
            answer = ', '.join(f"{model.names[int(c)]}" for i, c in enumerate(cls))
            messages = f'Success!'
            

    except Exception as e:
        answer = ''
        messages = str(e)

    logging.info(f'Messages:{messages}. Answer:{answer}.')
    to_api_dict = {}
    to_api_dict['messages'] = messages
    to_api_dict['answer'] = answer

    return jsonify(to_api_dict)

if __name__ == '__main__':

    app.run(port=5000, debug=False, threaded=True)
#%%