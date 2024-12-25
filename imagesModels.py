from ultralytics import YOLO
import cv2

# Modeli seç ve başlat
model = YOLO('yolov8n.pt')  # 'n' = nano, hızlı ve küçük model

# Modeli eğit
model.train(
    data='dataset.yaml',  # Veri kümenizi tanımlayan YAML dosyası
    epochs=50,         # Eğitim sayısı
    imgsz=640,         # Görüntü boyutu
    device='cpu'         # GPU kullanımı için
)
results = model.predict(source='test_image.jpg', conf=0.5)
results.show()
# Modeli kaydet
model.save('path_to_save_model/best_model.pt')

