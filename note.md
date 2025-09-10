# 環境
pyenv install 3.10.0
pyenv global 3.10.0
cd 要件環境的資料夾
pip install virtualenv
virtualenv YOLOv10

# 下載yolov10整包
.\YOLOv10\Scripts\activate.ps1
cd YOLO資料夾
pip install -r requirement.txt
# yolov10支援的CUDA版本:v11.8

# 原CUDA為12.6
下載:
https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local

安裝及設定環境變數
https://medium.com/@zera.tseng888/%E5%9C%A8windows11%E7%92%B0%E5%A2%83%E4%B8%8B%E5%AE%89%E8%A3%9Dcuda%E8%88%87cudnn-dd85575187ae

確認安裝成功
nvcc -V

python安裝符合CUDA 11.8的相關torch套件

# YOLO官網下載權重檔

# 測試環境流程
將已開發完的環境輸出packages:pip freeze > requirements_new.txt
退出環境: deactivate
建立新環境: python -m venv yolo_test
啟動環境: .\yolo_test\Scripts\activate
建立離線可安裝的packages:
    mkdir offline_packages
    注意: torch、torchvision、torchaudio因帶有+cu118，無法從 PyPI只能從PyTorch取得，故需分開下載
    pip download torch==2.0.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
    pip download torchvision==0.15.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
    pip download torchaudio==2.0.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html -d offline_packages
    刪除requirements_new.txt內的torch、torchvision、torchaudio，建立新的requirements_new_without_torch.txt
    pip download -r requirements_without_torch.txt -d offline_packages

echo Install CUDA related packages...
pip install --no-index --find-links=offline_packages torch==2.0.1+cu118
pip install --no-index --find-links=offline_packages torchvision==0.15.2+cu118
pip install --no-index --find-links=offline_packages torchaudio==2.0.2+cu118

echo Install the rest of the packages
pip install --no-index --find-links=offline_packages -r requirements_new_without_torch.txt


