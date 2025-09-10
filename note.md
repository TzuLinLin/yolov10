# YOLOv10 環境建置筆記

## 1. Python 環境安裝

```bash
pyenv install 3.10.0
pyenv global 3.10.0
cd <要建立環境的資料夾>
pip install virtualenv
virtualenv YOLOv10
```

---

## 2. 下載 YOLOv10 原始碼與啟動環境

```bash
.\YOLOv10\Scripts\activate.ps1
cd <YOLO資料夾>
pip install -r requirement.txt
```
> YOLOv10 支援的 CUDA 版本：**v11.8**

---

## 3. CUDA 安裝與設定

- 原 CUDA 版本：12.6
- 下載 CUDA 11.8：[官方下載頁](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)
- 安裝及設定環境變數：[Medium 教學](https://medium.com/@zera.tseng888/%E5%9C%A8windows11%E7%92%B0%E5%A2%83%E4%B8%8B%E5%AE%89%E8%A3%9Dcuda%E8%88%87cudnn-dd85575187ae)

### 驗證 CUDA 安裝
```bash
nvcc -V
```

---

## 4. 安裝符合 CUDA 11.8 的 Python torch 套件

---

## 5. 下載 YOLO 官方權重檔

---

## 6. 測試環境流程

1. 將已開發完的環境輸出 packages：
    ```bash
    pip freeze > requirements_new.txt
    ```
2. 退出環境：
    ```bash
    deactivate
    ```
3. 建立新環境：
    ```bash
    python -m venv yolo_test
    ```
4. 啟動新環境：
    ```bash
    .\yolo_test\Scripts\activate
    ```
5. 建立離線可安裝的 packages：
    ```bash
    mkdir offline_packages
    ```
    > 注意：torch、torchvision、torchaudio 因帶有 +cu118，無法從 PyPI，只能從 PyTorch 官網取得，故需分開下載。

    ```bash
    pip download torch==2.0.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
    pip download torchvision==0.15.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
    pip download torchaudio==2.0.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
    ```

    - 刪除 requirements_new.txt 內的 torch、torchvision、torchaudio，建立新的 requirements_new_without_torch.txt
    - 下載其餘套件：
      ```bash
      pip download -r requirements_new_without_torch.txt -d offline_packages
      ```

6. 安裝 CUDA 相關套件：
    ```bash
    pip install --no-index --find-links=offline_packages torch==2.0.1+cu118
    pip install --no-index --find-links=offline_packages torchvision==0.15.2+cu118
    pip install --no-index --find-links=offline_packages torchaudio==2.0.2+cu118
    ```

7. 安裝其餘套件：
    ```bash
    pip install --no-index --find-links=offline_packages -r requirements_new_without_torch.txt
    ```

---