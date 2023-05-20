import matplotlib.pyplot as plt
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

def audio_fft():
    # start = t.time()
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    n = len(data)
    x = np.linspace(0, 44100 / 2, int(n / 2))
    y = fft.fft(data) / n
    y = np.abs(y)
    y = y[range(int(n / 2))]
    # end = t.time()
    # cal_time = end - start
    # print(cal_time)

    return {"x": x, "y": y}

# main
while True:
    fft_data = audio_fft()
    for y in fft_data["y"]:
        if y > 100:
            print(list(fft_data["y"]).index(y))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(0, 10000)
    ax.set_ylim(0, 1000)
    ax.plot(fft_data["x"], fft_data["y"])

    plt.show()
