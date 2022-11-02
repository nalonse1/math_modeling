import numpy as np

arseniylox = np.zeros(5)
a = int(input('место в массиве '))
b = int(input('число в массив '))
for i in range(4):
    arseniylox[i] = int(input('числа массива '))
k = arseniylox[-2]
for i in range(a , 4):
    arseniylox[i + 1] = arseniylox[i]
arseniylox[-1] = k
arseniylox[a] = b
print(arseniylox)