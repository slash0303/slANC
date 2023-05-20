import pyaudio
import numpy as np
from numpy import fft
import scipy
import winsound
import time as t

# pyaudio initalize
CHUNK = 1024    # same as 'frames per buffer'
RATE = 44100    # sampling rate
FORMAT = pyaudio.paInt16
CHANNELS = 1
INPUT = True

# pyAudio object generate
p = pyaudio.PyAudio()
stream = p.open(frames_per_buffer=CHUNK,
                rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=INPUT,
                input_device_index=0,)

# main
while True:
    start = t.time()
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    n = len(data)
    x = np.linspace(0, 44100 / 2, int(n / 2))
    y = fft.fft(data) / n
    y = np.abs(y)
    y = y[range(int(n / 2))]
    end = t.time()
    cal_time = end - start
    print(cal_time)