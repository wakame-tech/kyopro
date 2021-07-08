from itertools import product
from functools import reduce

n, k = list(map(int, input().split()))
ts = []
for i in range(n):
    t = list(map(int, input().split()))
    ts.append(t)

for i in product(*ts):
    if reduce(lambda a, b: a ^ b, i) == 0:
        print('Found')
        break
else:
    print('Nothing')