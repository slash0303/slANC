import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from eaxtension import LogE

fig = plt.figure()
ax = plt.axes(xlim = (0, 2), ylim = (-2, 2))
line, = ax.plot([], [], lw=3)

def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    LogE.g("Line,", line,)
    LogE.d("Line", line)
    return line,

anim = FuncAnimation(fig, animate, frames=200, interval=50)

plt.show()