import speech_recognition as sr
import sounddevice as sd
import numpy as np
import time

init_rec = sr.Recognizer()

def print_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10


def recognize_speech():
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio_data = init_rec.listen(source)  # Dinlemeye başla
        try:
            text = init_rec.recognize_google(audio_data, language="tr-TR")
            print(f'Tanınan metin: {text}')
        except sr.UnknownValueError:
            print("Anlaşılamadı, lütfen tekrar konuşun.")
        except sr.RequestError:
            print("Google API'ye erişim sağlanamadı.")

with sd.InputStream(callback=print_volume):
    try:
        while True:
            recognize_speech()
            time.sleep(1)  # Her dinlemeden sonra 1 saniye bekle
    except KeyboardInterrupt:
        print("Programdan çıkılıyor...")
