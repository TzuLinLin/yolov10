@echo off
echo Install Python 3.10
pyenv install 3.10.0
pyenv global 3.10.0
pip install virtualenv

echo With an Internet connection, download the YOLOv10 source code
cd D:\workspace
git clone https://github.com/THU-MIG/yolov10.git

echo Build environment...
cd D:\workspace\yolov10
virtualenv yolo_env

echo Activate environment...
.\yolo_env\Scripts\activate

echo Install packages...
pip install --no-index --find-links=offline_packages -r requirements.txt

echo Finish!
pause