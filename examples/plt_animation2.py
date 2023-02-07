import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim=(0, 3), ylim=(0, 9))

a = np.arange(0, 3, 0.2)
ax.plot(a, a**2)

redDot, = plt.plot([], [], 'ro')

def animate(frame):
    redDot.set_data(frame, frame**2)
    return redDot

ani = FuncAnimation(fig, animate, frames=np.array([0.2, 0.4, 0.6]))

plt.show()