import numpy as np

N = int(input())
M = int(input())
arseniylox = np.zeros((N, M))
for i in range (N):
    for j in range(M):
        if i == 1 and j == 1:
            arseniylox[i, j] = np.sin(N * i + M * j)
        else:
            arseniylox[i, j] = np.sin(N * (i+1) + M * (j + 1)) 
print(arseniylox)