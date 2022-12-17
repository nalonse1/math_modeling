import matplotlib.pyplot as plt 
import numpy as np 

def artemy(xa, xb, N, *args, **kwargs):

    if kwargs["xoba"] == "c":
        x = np.arange( xa*args[0], xb*args[0], N)
        y = np.arange( xa*args[0], xb*args[0], N)   
        x1, y1= np.meshgrid(x, y)
        fxy = x1**2 + y1**2 - args[0]**2





    plt.contour(x1, y1, fxy, levels=[0])
    plt.savefig("pic_4")
    plt.axis('equal')

artemy(2, -2, 0.01, 10, xoba = 'c')
