import speech_recognition as sr
import pyttsx3  # Metni konuşmaya çeviren kütüphane

r = sr.Recognizer()  # speech_recognition için recognizer nesnesi tanımlama

# Konuşmayı metine çeviren ve ekrana yazan fonksiyon
def SpeechToText(stt_mic):        
    print("Konuşun:")
    # Recognizer'ın çevredeki gürültü seviyesine göre enerji eşiğini ayarlamasına izin vermek için bir saniye bekleme 
    r.adjust_for_ambient_noise(stt_mic, duration=0.2)			  
    audio = r.listen(stt_mic)  # Kullanıcı girişini alma

    text = r.recognize_google(audio, language='tr-TR')  # Google ile sesi metine çevirme
    text = text.lower()  # Metni küçük harfe çevirme
    print(f"Alınan metin: {text}")  # Metni ekrana yazma	
    return text

# Metni konuşmaya çeviren ve oynatan fonksiyon
def TextToSpeech(tts_text):        
    engine = pyttsx3.init()  # pyttsx3 motorunu başlat
    engine.setProperty('rate', 150)  # Konuşma hızını ayarla (isteğe bağlı)
    engine.setProperty('volume', 1)  # Ses seviyesini ayarla (isteğe bağlı)
    engine.say(tts_text)  # Metni konuşmaya çevir
    engine.runAndWait()  # Konuşmanın bitmesini bekle

try:
    while True:
        with sr.Microphone() as mic:  # Giriş kaynağı olarak mikrofon kullanma
            text = SpeechToText(mic)  # Konuşmayı metine çevirme ve ekrana yazma
            TextToSpeech(text)  # Metni konuşmaya çevirme ve oynatma                  

except KeyboardInterrupt:  # Ctrl-C ile çıkış
    pass
