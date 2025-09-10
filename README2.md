# YOLOv10 離線推論 API 專案

此專案建立一個基於 Flask 的 Restful API，使用 YOLOv10 模型進行物件偵測，需在CUDA 11.8 + Windows10下進行，並確保CUDA11.8與 GPU 驅動相容。


## 程式架構

```
yolov10/
├── offline_packages/         ← 在有網路下，依requirements.txt先下載好的套件 (whl檔)
├── weights/
│   └── yolov10n.pt           ← YOLOv10 預訓練模型(需先下載好)
├── images/                   ← 測試用圖片資料夾（1280x720）
├── server.py                 ← 伺服器端推論服務
├── client.py                 ← 用戶端發送圖片至伺服器取得推論結果
├── config.ini                ← 模型參數設定檔
├── logs/
│   └── 2025-05-13.log        ← 程式執行log檔
├── yolo_env                  ← 執行install_env.bat後建立的環境
├── requirements.txt          ← 所需套件
├── install_env.bat           ← 程式安裝流程，(環境/套件)執行檔
└── README.md                 ← 專案說明文件
```


