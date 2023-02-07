import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy

# pyaudio initalize
CHUNK = 1024    # same as 'frames per buffer'
RATE = 44100    # sampling rate
FORMAT = pyaudio.paInt32
CHANNELS = 1
INPUT = True

# matplotlib axes initalize
fig = plt.figure()
ax = fig.add_subplot()
ax.set_title("Fast Fourier Transfer")
ax.set_xlim((0,5000))   # x
ax.set_xlabel("Frequency level")
ax.set_ylim((0,10000))  # y
ax.set_ylabel("Amplitude level")

# matplotlib animation function
line, = ax.plot([], [], lw=3)

def animate(frame):
    x = np.linspace(0, 4, 5000)
    y = np.sin(2 * np.pi * (x - 0.01 * frame))
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, frames=200, interval=100)

plt.show()