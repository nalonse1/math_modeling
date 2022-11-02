from lab_3_task_1 import g
import numpy as np


x0 = int(input())
y0 = int(input())
v = int(input())
t = np.arange(0, 5, 0.001)
x = x0 + v * t
y = y0 - (g * (t ** 2)) / 2 + v * t
print(t)