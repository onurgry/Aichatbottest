from gtts import gTTS
import os
import playsound
import time
def speak(text):
    tts = gTTS(text=text, lang='tr')
    
    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(r"C:\Users\Izoly\Desktop\yz\abc.mp3")
    time.sleep(3)
    os.remove(filename)

speak("merhaba dünya")