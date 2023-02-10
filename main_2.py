import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy
from eaxtension import LogE

# pyaudio initalize
CHUNK = 2000    # same as 'frames per buffer'
RATE = 44100    # sampling rate
FORMAT = pyaudio.paInt16
CHANNELS = 1
INPUT = True

# matplotlib axes initalize
fig = plt.figure()
ax = fig.add_subplot()
ax.set_title("Fast Fourier Transfer")
ax.set_xlim((0,5000))   # x
ax.set_xlabel("Frequency level")
ax.set_ylim((0,1000))  # y
ax.set_ylabel("Amplitude level")

# matplotlib animation function
line, = ax.plot([], [], lw=3)

p = pyaudio.PyAudio()
stream = p.open(frames_per_buffer=CHUNK,
                rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=INPUT,
                input_device_index=23,)

def init():
    line.set_data([], [])
    LogE.g("init", "init function activated")
    return line,

def animate(frame):
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    n = len(data)
    x = np.linspace(0, 44100 / 2, int(n/2))
    y = np.fft.fft(data) / n
    y = np.abs(y)
    y = y[range(int(n / 2))]
    line.set_data(x, y)
    LogE.d("animate", "animate function activated")
    return line

ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=10, blit=False)

plt.show()