import numpy as np

N = int(input('количество строк '))
M = int(input('количство столбцов '))

arseniylox = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        arseniylox[i,j] = int(input('числа 1 массива '))
for i in range(M):
    print(arseniylox ,max(arseniylox[ : , i]))