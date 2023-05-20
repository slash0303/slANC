import pyaudio
import numpy as np
from numpy import fft
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy
# from eaxtension import LogE
from eaxtension import jsonE
# from eaxtension import timeE
import winsound
import time as t

# pyaudio initalize
CHUNK = 1024    # same as 'frames per buffer'
RATE = 44100    # sampling rate
FORMAT = pyaudio.paInt16
CHANNELS = 1
INPUT = True

# matplotlib axes initalize
fig = plt.figure(figsize=(15, 5))

ax_fft = fig.add_subplot(1, 2, 1)
ax_fft.set_title("Fast Fourier Transform")
ax_fft.set_xlim((0,10000))   # x
ax_fft.set_xlabel("Frequency level")
ax_fft.set_ylim((0,1000))  # y
ax_fft.set_ylabel("Amplitude level")

ax_phase = fig.add_subplot(1, 2, 2)
ax_phase.set_title("Phase of sound")
phase_x_sec = 0
phase_x_space = 10
ax_phase.set_xlim((phase_x_sec, phase_x_sec + phase_x_space))
ax_phase.set_xlabel(f"Time ({phase_x_space}s)")
ax_phase.set_ylim((-15000, 15000))
ax_phase.set_ylabel("Amplitude")

# matplotlib animation function
line_fft, = ax_fft.plot([], [], lw=3)
line_phase, = ax_phase.plot([], [], lw=3)

# pyAudio object generate
p = pyaudio.PyAudio()
stream = p.open(frames_per_buffer=CHUNK,
                rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=INPUT,
                input_device_index=0,)

# fft_animation initalize function
def init_fft():
    line_fft.set_data([], [])
    return line_fft,

# fft animation for Funcanimation
def animate_fft(frame):
    start = t.time()
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    n = len(data)
    # LogE.d("data", data)
    x = np.linspace(0, 44100 / 2, int(n/2))
    y = fft.fft(data) / n
    y = np.abs(y)
    y = y[range(int(n / 2))]
    # LogE.d("x", x)
    # LogE.d("y", y)
    line_fft.set_data(x, y)
    jsonE.dumps("fft_data", {"data" : str(data), "x" : str(x), "y" : str(y), "pyaudio": str(stream.read(CHUNK))})
    end = t.time()
    cal_time= end-start
    print(cal_time)

    return line_fft,

# phase function initalize function
def init_phase():
    line_phase.set_data([], [])
    return line_phase,

# phase animation for Funcanimation
def animate_phase(frame):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    n = len(data)
    x = np.linspace(0, 10, int(n/2))
    y = data[range(int(n/2))]
    line_phase.set_data(x, y)

    return line_phase,

# sfx - start
file_name = "res/start_sfx.wav"
winsound.PlaySound(file_name, winsound.SND_FILENAME)

# plotting animation
ani_fft = FuncAnimation(fig, animate_fft, init_func=init_fft, interval=50, frames=60, blit=True)
ani_phase = FuncAnimation(fig, animate_phase, init_func=init_phase, interval=50, frames=60, blit=True)
plt.show()