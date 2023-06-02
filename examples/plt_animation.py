import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(2*np.pi*(x - 0.01*frame))
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
plt.show()
