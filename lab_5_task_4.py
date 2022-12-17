import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 0)
y =np.arange(0, -10) 
plt.plot(x, y, color='g', label='luchte', marker='>', ms=1)
plt.xlabel('coord: x')
plt.ylabel('coord: y')
plt.legend()
plt.title('base')
plt.grid()
plt.show()
plt.savefig('pic_4.png')