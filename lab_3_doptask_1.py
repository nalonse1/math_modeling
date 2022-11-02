import numpy as np

N = int(input('количество строк '))
M = int(input('количство столбцов '))
arseniylox = np.zeros((N, M))
kirilllox = np.zeros((N, M))
xobalox = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        arseniylox[i,j] = int(input('числа 1 массива '))
for i in range(N):
    for j in range(M):
        kirilllox[i,j] = int(input('числа 2 массива '))
for i in range(N):
    for j in range(M):
        if arseniylox[i,j] > kirilllox[i,j]:
            xobalox[i,j] = arseniylox[i,j]
        else:
            xobalox[i,j] = kirilllox[i,j]

print(xobalox)