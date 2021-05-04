import numpy as np

blocks = []

a = [1, 2, 3]
a.extend([4, 5])
# a = [1, 2, 3, 4, 5]

h, w = map(int, input().split())
for i in range(h):
    b = list(map(int, input().split()))
    blocks.append(b)

print(np.sum(blocks - np.min(blocks)))