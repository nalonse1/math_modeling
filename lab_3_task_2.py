import numpy as np
from lab_3_task_1 import g, k, e

h = 100
a = np.pi / 3
b = np.pi / 6
T = 200 * k
l = 300

lox = np.sqrt(g * h * np.tan(b) ** 2)
lox2 = np.sqrt(2 * np.cos(a) ** 2 * (1 - np.tan(b) * np.tan(a)))
v = lox / lox2
print(v)

n = (2 / np.pi) * (h / (k * T) ** (3 / 2)) * e ** (-l / k / T) * l ** (T / 2)

print(n)