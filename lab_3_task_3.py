from lab_3_task_1 import g
import numpy as np

lst =[]
x0 = int(input())
y0 = int(input())
v = int(input())
for t in range (1 , 5, 1):
    x = x0 + v * t
    y = y0 - (g * (t ** 2)) / 2 + v * t
    lst.append((t, x, y))
arseniylox = np.array(lst)
print(arseniylox)
