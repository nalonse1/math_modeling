import numpy as np

arseniylox = np.zeros(5)
a = int(input('место в массиве '))
b = int(input('число в массив '))
for i in range(5):
    arseniylox[i] = int(input('числа массива '))
arseniylox[a-1] = b
print(arseniylox)
