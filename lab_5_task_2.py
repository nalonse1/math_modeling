import matplotlib.pyplot as plt 
import numpy as np 

def artemy(xa, xb, N, *args, **kwrgs):
    x= np.arange(xa, xb, N)
    if kwrgs["xoba"] == "p":
        title = "hyperbola"
        y = args[0] * x ** 2 + args[1] * x + args[2]
    elif kwrgs["xoba"] == "h":
        y = args[0] / (args[1]*x)
        title = "hyperbola"

    plt.plot(x, y)
    plt.xlabel('coord: x')
    plt.ylabel('coord: y')
    plt.title(title)
    plt.axis('equal')
    plt.savefig('pic_3.png')

artemy(0.1, 10, 0.1, 1, 1,   xoba = 'h')