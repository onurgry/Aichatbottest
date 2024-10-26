#26.10.2024 Onur Güray
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import time
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template="""
Aşağıdaki soruya kısa cevap ver.

Konuşma geçmişi şu şekilde: {context}

Soru: {question}

Cevap:
"""

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
            context += f"\nUser: {text}\nYapayZeka: {result}"
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
