import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a=1, b=1, c=0, title=("parabola_plotter")):
    x = np.arange(-10, 10, 0.01)
    y=a*x**2 + b*x + c

    plt.plot(x, y, label= "my parabola")    
    plt.xlabel('coord: x')
    plt.ylabel('coord: y')
    plt.legend()
    plt.title('title')
    plt.grid()
    plt.savefig("pic_1.png")
    
parabola_plotter()