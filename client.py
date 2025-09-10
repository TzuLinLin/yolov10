#%%
import os
import time
import base64
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
#%%
url = "http://127.0.0.1:5000/img"  
p = Path(__file__).resolve().parent /'images'

#%%
def send_image(file):
    with open(file, "rb") as f:
        # 編碼成base64格式避免路徑依賴與檔案格式問題
        img_b64 = base64.b64encode(f.read()).decode('utf-8')
    data = {"IMG": img_b64}
    response = requests.post(url, json=data)
    return file.name, response.json()

s = time.time()
files = [file for file in p.glob('*') if file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']]

with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor: 
    futures = [executor.submit(send_image, file) for file in files]
    for future in as_completed(futures):
        fname, result = future.result()
        print(f"{fname}: {result}")
        
print(f"Time taken: {time.time()-s:.2f}s")
#%%