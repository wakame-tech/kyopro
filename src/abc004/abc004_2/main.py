import numpy as np

c = []
for i in range(4):
    c.append(input().split())
c = np.array(c)
c = np.rot90(c, 2)
for i in range(4):
    print(' '.join(c[i, :]))