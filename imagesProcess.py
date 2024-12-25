import os
from sklearn.model_selection import train_test_split

# Görüntü dosyalarının bulunduğu dizin
image_dir = r"C:\\Users\\melda\Documents\\GitHub\\Görüntü-işleme\\Goruntu-isleme\dataset\\images"

# Tüm .jpg dosyalarını bul
image_paths = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.jpeg')]

# Eğitim ve test veri setlerini ayır
train, test = train_test_split(image_paths, test_size=0.2, random_state=42)

# Eğitim dosyalarını yaz
with open('train.txt', 'w') as train_file:
    train_file.writelines([f"dataset/images/{img}\n" for img in train])

# Test dosyalarını yaz
with open('test.txt', 'w') as test_file:
    test_file.writelines([f"dataset/images/{img}\n" for img in test])

print("Veri seti başarıyla bölündü ve kaydedildi!")
