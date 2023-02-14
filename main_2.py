import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy
from eaxtension import LogE
from eaxtension import jsonE
import winsound

# pyaudio initalize
CHUNK = 2000    # same as 'frames per buffer'
RATE = 44100    # sampling rate
FORMAT = pyaudio.paInt16
CHANNELS = 1
INPUT = True

# matplotlib axes initalize
fig = plt.figure()
ax = fig.add_subplot()
ax.set_title("Fast Fourier Transform")
ax.set_xlim((0,10000))   # x
ax.set_xlabel("Frequency level")
ax.set_ylim((0,1000))  # y
ax.set_ylabel("Amplitude level")

# matplotlib animation function
line, = ax.plot([], [], lw=3)

# pyAudio object generate
p = pyaudio.PyAudio()
stream = p.open(frames_per_buffer=CHUNK,
                rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=INPUT,
                input_device_index=0,)

# FuncAnimation initalize function
def init():
    line.set_data([], [])
    return line,

# FuncAnimation main function
def animate(frame):
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    n = len(data)
    LogE.d("data", data)
    x = np.linspace(0, 44100 / 2, int(n/2))
    y = np.fft.fft(data) / n
    y = np.abs(y)
    y = y[range(int(n / 2))]
    LogE.d("x", x)
    LogE.d("y", y)
    line.set_data(x, y)
    jsonE.dumps("fft_data", {"data" : str(data), "x" : str(x), "y" : str(y)})
    return line

# sfx
file_name = "res/start_sfx.wav"
winsound.PlaySound(file_name, winsound.SND_FILENAME)

ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=10, blit=False)

plt.show()