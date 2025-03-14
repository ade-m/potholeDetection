# Deteksi Lubang Jalan dengan YOLO

Proyek ini menggunakan model YOLO untuk mendeteksi lubang jalan (pothole) secara otomatis dari video.

## 📌 Fitur
- Deteksi lubang jalan menggunakan YOLOv8.
- Segmentasi objek untuk mendapatkan bentuk lubang yang lebih akurat.
- Pemrosesan video dengan rotasi dan resize otomatis.

## 🔧 Instalasi
1. Pastikan Python 3.x sudah terinstal.
2. Install dependensi dengan menjalankan perintah berikut:
   ```bash
   pip install opencv-python torch ultralytics huggingface_hub
   ```
3. Unduh model dari Hugging Face:
   ```python
   from huggingface_hub import hf_hub_download
   model_path = hf_hub_download("keremberke/yolov8m-pothole-segmentation", filename="best.pt")
   ```
4. Jalankan skrip dengan:
   ```bash
   python detect_pothole.py
   ```

## 📂 Struktur Proyek
```
├── asset/
│   ├── IMG_1944.MOV  # Contoh video input
├── detect_pothole.py  # Skrip utama
├── README.md  # Dokumentasi proyek
```

## 🎯 Penggunaan
1. Letakkan video yang ingin dianalisis di dalam folder `asset/`.
2. Jalankan skrip `detect_pothole.py`.
3. Sistem akan menampilkan hasil deteksi lubang jalan secara real-time.

## 🔗 Model YOLO untuk Pothole
Model yang digunakan dalam proyek ini tersedia di Hugging Face:
[YOLOv8m Pothole Segmentation](https://huggingface.co/keremberke/yolov8m-pothole-segmentation)

## 📢 Sosial Media
- TikTok: [@ademaulana_4](https://www.tiktok.com/@ademaulana_4)
- Instagram: [@ademaulana_](https://www.instagram.com/ademaulana_/)
- YouTube: [@ademaulana_4](https://www.youtube.com/@ademaulana_4)

Jangan lupa follow untuk update proyek terbaru! 🚀

