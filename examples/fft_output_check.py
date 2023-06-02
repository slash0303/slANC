import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.arange(0, 3, 1 / fs)
f1 = 35
f2 = 10
signal = 0.6 * np.sin(2 * np.pi * f1 * t) + 3 * np.cos(2 * np.pi * f2 * t + np.pi / 2)

fft = np.fft.fft(signal) / len(signal)

fft_magnitude = abs(fft)

length = len(signal)
f = np.linspace(-(fs / 2), fs / 2, length)

plt.stem(f, np.fft.fftshift(fft_magnitude))
plt.ylim(0, 2.5)
plt.grid()

plt.show()

print()