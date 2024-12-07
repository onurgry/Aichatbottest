#7.12.2024 Onur Güray
import speech_recognition as sr
import sounddevice as sd
import numpy as np
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from gtts import gTTS
import os
import playsound
import time

template="""
Bir restorantın siparişlerini alıyorsun
restorant pazar günleri kapalı
haftanın diğer günleri akşam saat sekizde kapatmakta
menü aşağıdaki şekilde
Lahmacun - 200 türk lirası
Salata - 50 türk lirası
Kola - 20 türk lirası
Kelle Paça Çorbası - 80 türk lirası
Az kelle paça çorbası - 40 türk lirası



Aşağıdaki soruya kısa cevap ver.
Emoji Kullanmadan sorulara kısa cevap ver
Konuşma geçmişi şu şekilde: {context}

Soru: {question}

Cevap:
"""
orders = []
model = OllamaLLM(model="gemma2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


init_rec = sr.Recognizer()

def print_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10


def recognize_speech():
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio_data = init_rec.listen(source)  # Dinlemeye başla
        try:
            context = ""
            text = init_rec.recognize_google(audio_data, language="tr-TR")
            print(f'Tanınan metin: {text}')
            result = chain.invoke({"context":context,"question":text})
            print("YapayZeka:",result)
            orders.append(text)
            context += f"\nUser: {text}\nYapayZeka: {result}"
        except sr.UnknownValueError:
            print("Anlaşılamadı, lütfen tekrar konuşun.")
        except sr.RequestError:
            print("Google API'ye erişim sağlanamadı.")
def summarize():
        

        # Yapay zeka ile özetleme
        context = "\n".join(orders)
        summary_prompt = "Aşağıdaki siparişlerin kısa bir özetini yap: {context}"
        summary_result = chain.invoke({"context": context, "question": summary_prompt})
        print("Yapay Zeka Özeti:", summary_result)
        with open("summary_output.txt", "w", encoding="utf-8") as file:
            file.write("Yapay Zeka Özeti:\n")
            file.write(summary_result)
            print("Özet dosyaya kaydedildi: summary_output.txt")
with sd.InputStream(callback=print_volume):
    try:
        while True:
            recognize_speech()
            time.sleep(0.5)  # Her dinlemeden sonra 1 saniye bekle
    except KeyboardInterrupt:
        summarize()
        time.sleep(0.5)
        print("Programdan çıkılıyor...")
