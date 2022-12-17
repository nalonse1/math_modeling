import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.axis('equal')

def cyc(R):
    t = np.arange(0, 8*np.pi, 0.1)
    x = R * t - (R * np.sin(t))
    y = R - R * np.cos(t)
    plt.plot(x, y, ls ="-", lw = 2)
    plt.savefig("pic_cyc.png")

def ast(R):
    t = np.arange(0, 2*np.pi, 0.1)
    x = R *  np.sin(t)**3
    y = R * np.cos(t)**3
    plt.plot(x, y, ls ="-", lw = 5)
    plt.savefig("pic_ast.png")



ast(3)
