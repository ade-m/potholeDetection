import cv2
import torch
from ultralytics import YOLO
from huggingface_hub import hf_hub_download

# Unduh model dari Hugging Face
repo_id = "keremberke/yolov8m-pothole-segmentation"
model_filename = "best.pt"

model_path = hf_hub_download(repo_id=repo_id, filename=model_filename)

# Load model YOLO
model = YOLO(model_path)

def correct_rotation(frame, cap):
    rotate_code = { 
        90: cv2.ROTATE_90_CLOCKWISE,
        180: cv2.ROTATE_180,
        270: cv2.ROTATE_90_COUNTERCLOCKWISE
    }
    try:
        rotation = int(cap.get(cv2.CAP_PROP_ORIENTATION_META))
        if rotation in rotate_code:
            frame = cv2.rotate(frame, rotate_code[rotation])
    except:
        pass
    return frame
def resize_frame(frame, scale=0.5):
    height, width = frame.shape[:2]
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized_frame


# Buka video input
video_path = "asset/IMG_1944.MOV"  # Ganti dengan path video Anda
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Tidak dapat membuka video.")
    exit()

frame_skip = 5  # Lewati setiap 2 frame untuk mengurangi beban
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Video selesai

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue  # Lewati frame untuk mengurangi FPS

    frame = correct_rotation(frame, cap)  
    frame = resize_frame(frame, scale=0.02)  

    # Deteksi pothole di frame
    results = model(frame)

    # Render hasil deteksi
    frame = results[0].plot()

    # Tampilkan hasil deteksi di layar
    cv2.imshow("Pothole Detection", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Tutup semua jendela
cap.release()
cv2.destroyAllWindows()
