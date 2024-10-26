import sounddevice as sd
import numpy as np
import time

def print_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm < 0.9:
        print("konuşmuyor")
    else:
        print("konuşuyor")


with sd.InputStream(callback=print_volume):
    try:
        while True:


            time.sleep(1)  
    except KeyboardInterrupt:
        print("Programdan çıkılıyor...")