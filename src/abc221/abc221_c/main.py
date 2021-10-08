import math
from itertools import permutations

n = input()
k = len(n)

ans = 0
for s in permutations(n):
    for i in range(1, k):
        a, b = s[:i], s[i:]
        # print(a, b)
        a, b = ''.join(a), ''.join(b)
        if a == '' or b == '' or a.startswith('0') or b.startswith('0'):
            continue
        a, b = int(a), int(b)
        if a == 0 or b == 0:
            continue

        ans = max(ans, a * b)

print(ans)
