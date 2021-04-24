# n = int(input())
# a = list(map(int, input().split()))
# ca = [0]
# for i in range(0, n):
#     ca.append(ca[i] + a[i])

# for k in range(1, n + 1):
#     print(max([ca[i] - ca[i - k] for i in range(k, n + 1)]))

import numpy as np
from time import time

# l = np.random.rand(10 ** 8)
l = [0] * (10 ** 8)
n = time()
# np.sum(l)
sum(l)
print(time() - n)