import matplotlib.pyplot as plt
import numpy as np

x = [1, 1, 5, 5, 1]
y = [1, 5, 5, 1, 1]

plt.plot(x, y, color='k', label='square', marker='>', ms=)
plt.axis('equal')
plt.xlabel('coord: x')
plt.ylabel('coord: y')

plt.savefig('pic_task_1.png')