import cv2
from ultralytics import YOLO

# Modeli yükleyin
model = YOLO('runs/detect/train/weights/best.pt')  # Eğitilmiş modelin yolunu belirtin

# Kamerayı açın
cap = cv2.VideoCapture(0)  # 0, varsayılan kamera

while True:
    ret, frame = cap.read()  # Kameradan bir görüntü al
    if not ret:
        break  # Görüntü alınamazsa çık

    # Modeli çalıştır
    results = model(frame)  # Kameradaki frame'i modelinize verin

    # Modelin çıktısından tespit edilen her nesne için döngü
    for result in results:
        # Her nesnenin tespit edilmesini işleyin
        for box in result.boxes:
            cls = int(box.cls[0])  # Nesnenin sınıfı
            label = model.names[cls]  # Nesnenin etiket ismi (implantlı/implantsız)
            confidence = box.conf[0]  # Güven skoru

            # Etiket ve güven skorunu yazdır
            print(f"Label: {label}, Confidence: {confidence:.2f}")

            # Tespit edilen nesneye çerçeve çiz
            x1, y1, x2, y2 = box.xyxy[0]  # Koordinatlar
            cv2.putText(frame, f"{label} ({confidence:.2f})", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # Sonuçları göster
    cv2.imshow('Frame', frame)

    # 'q' tuşuna basarak çıkabilirsiniz
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Kamerayı serbest bırak
cv2.destroyAllWindows()  # Pencereleri kapat
