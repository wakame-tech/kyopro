import numpy as np

w, h, n = list(map(int, input().split()))
g = np.zeros((w, h))
for i in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        g[:x, :] = 1
    if a == 2:
        g[x:, :] = 1
    if a == 3:
        g[:, :y] = 1
    if a == 4:
        g[:, y:] = 1
        
print((w * h) - int(np.sum(g)))
