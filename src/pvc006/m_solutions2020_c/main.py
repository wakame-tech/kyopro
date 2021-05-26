
import numpy as np

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

p = np.product(a[:k + 1])
for i in range(k + 1, n):
    newp = p // a[i - (k + 1)] * a[i]
    print('Yes' if p < newp else 'No')
    p = newp