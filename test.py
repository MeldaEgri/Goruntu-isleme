import cv2
from ultralytics import YOLO

# Eğitilmiş modeli yükle
model = YOLO('runs/detect/train/weights/best.pt')  # Eğitilmiş modelin yolunu belirtin

# Kamera açma
cap = cv2.VideoCapture(0)  # 0, varsayılan kamerayı belirtir

while True:
    ret, frame = cap.read()  # Kameradan bir görüntü oku
    if not ret:
        print("Kameradan görüntü alınamadı.")
        break

    # Modeli görüntü üzerinde çalıştır
    results = model.predict(source=frame, conf=0.5, show=False)  # Tahminleri yap
    annotated_frame = results[0].plot()  # Etiketlenmiş görüntüyü al

    # Tespit edilen sınıfları ekrana yazdır
    for box in results[0].boxes:
        cls = int(box.cls[0])  # Tahmin edilen sınıfın ID'si
        label = results[0].names[cls]  # Sınıfın adı (implantlı veya implantsız)
        print(f"Tespit edilen sınıf: {label}")

    # Sonuçları ekranda göster
    cv2.imshow("Kamera", annotated_frame)

    # 'q' tuşuna basarak çıkabilirsiniz
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Kamerayı serbest bırak
cv2.destroyAllWindows()  # Açılan tüm pencereleri kapat
