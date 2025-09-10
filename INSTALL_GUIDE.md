# YOLOv10 + CUDA 11.8 + 環境安裝指南（Windows10 適用）

---
## 1. 安裝相關環境（使用 pyenv）

```bash
. install_env.bat
```
---
## 2. Activate environment.

```bash
cd .\yolov10
.\yolo_env\Scripts\activate
```
---



## ⚙️ 4. 安裝 CUDA 11.8（若當前 CUDA 為 12.x）

- 下載位置：
  👉 https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local

- 安裝與環境變數設定教學：
  👉 https://medium.com/@zera.tseng888/在windows11環境下安裝cuda與cudnn-dd85575187ae

- 驗證安裝：
```bash
nvcc -V
```

---

## 🔁 5. 匯出並建立可離線安裝環境

### ✅ 5.1 匯出已完成的套件列表

```bash
pip freeze > requirements_new.txt
deactivate
```

### ✅ 5.2 建立測試環境並啟動

```bash
python -m venv yolo_test
.\yolo_test\Scriptsctivate
```

---

## 📁 6. 準備離線安裝套件

### 🔸 6.1 建立資料夾

```bash
mkdir offline_packages
```

### 🔸 6.2 分開下載含 CUDA 的 PyTorch 套件（**這些無法從 PyPI 安裝**）

```bash
pip download torch==2.0.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
pip download torchvision==0.15.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
pip download torchaudio==2.0.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
```

### 🔸 6.3 移除原始 requirements 中的 torch 套件

- 編輯 `requirements_new.txt`，移除：
  - `torch`
  - `torchvision`
  - `torchaudio`

- 存成新檔案：
```txt
requirements_without_torch.txt
```

### 🔸 6.4 下載其餘依賴套件

```bash
pip download -r requirements_without_torch.txt -d offline_packages
```

---

## 📦 7. 離線安裝全套套件（使用 install_offline.bat）

### 建立 `install_offline.bat`

```bat
@echo off
python -m venv venv
call venv\Scriptsctivate

echo 安裝 PyTorch CUDA 相關套件...
pip install --no-index --find-links=offline_packages torch==2.0.1+cu118
pip install --no-index --find-links=offline_packages torchvision==0.15.2+cu118
pip install --no-index --find-links=offline_packages torchaudio==2.0.2+cu118

echo 安裝其餘套件...
pip install --no-index --find-links=offline_packages -r requirements_without_torch.txt

echo ✅ 安裝完成！
pause
```

---

## 📥 8. YOLOv10 模型與 TensorRT 引擎轉換（可選）

1. 匯出 ONNX：
```bash
python export.py --weights yolov10n.pt --img 640 --batch 1 --device 0 --include onnx
```

2. 使用 trtexec 轉換為 TensorRT `.engine`：
```bash
trtexec --onnx=yolov10n.onnx --saveEngine=yolov10n.engine --fp16
```

---

## ✅ 9. 測試環境

1. 啟動伺服器：
```bash
python server.py
```

2. 執行 Client：
```bash
python client.py
```

---

## 📝 備註

- 測試圖片請放在 `test_images/` 目錄中。
- 模型預訓練權重請放於 `models/yolov10n.pt` 或 `yolov10n.engine`。
- 若有安裝錯誤，請檢查 CUDA 驅動版本與 Python 相容性。
