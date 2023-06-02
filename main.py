import matplotlib.pyplot as plt
import pyaudio
import numpy as np
from numpy import fft
import scipy
import winsound
import time as t
from eaxtension import jsonE
from collections import defaultdict

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
    x = np.linspace(0, 44100 / 2, n//2)
    y = fft.fft(data) / n
    y = np.abs(y)
    y = y[range(int(n / 2))]
    # end = t.time()
    # cal_time = end - start
    # print(cal_time)
    # TODO 주파수 대역 좁히고 밀도 올리기
    return {"x": x, "y": y}

def fft_plot():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title("Fast Fourier Transform")
    ax.set_xlim(0, 10000)
    ax.set_xlabel("Frequency level")
    ax.set_ylim(0, 1000)
    ax.set_ylabel("Amplitude level")
    ax.plot(fft_data["x"], fft_data["y"])
    plt.show()

def noise_plot(x_data:dict):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title("Count of noise detection")
    ax.set_xlim((0, 10000))
    ax.set_xlabel("Frequency level")
    ax.set_ylabel("count")
    ax.hist(x_data, bins=10000)     # TODO 사용되지 않는 주파수 대역 찾아내기
    plt.show()


# main
noise_data = defaultdict(int)
noise_list = []

max_time = 10   # sec

try:
    start_time = t.time()
    while True:
        mes_time = t.time() - start_time
        print(mes_time)
        if mes_time > max_time:
            break
        fft_data = audio_fft()
        for i, y in enumerate(fft_data["y"]):
            if y > 3:
                data_x = fft_data["x"][i]
                # print(i, ",", data_x)
                try: noise_data[data_x] += 1
                except: noise_data[data_x] = 1
                noise_list.append(data_x)
        # fft_plot()
    noise_data["noise_list"] = noise_list
    # print(noise_data)
    jsonE.dumps("noise_data", noise_data)
    noise_plot(noise_list)
except:
    noise_data["noise_list"] = noise_list
    # print(noise_data)
    jsonE.dumps("noise_data", noise_data)
    noise_plot(noise_list)