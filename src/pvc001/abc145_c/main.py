from itertools import permutations
import math

n = int(input())
ps = []
for i in range(n):
    x, y = map(int, input().split())
    ps.append((x, y))


def dis(a):
    d = 0
    for i in range(1, len(a)):
        d += math.sqrt((a[i][0] - a[i - 1][0]) ** 2 + (a[i][1] - a[i - 1][1]) ** 2)
    return d


s = 0
cnt = 0
for p in permutations(ps):
    cnt += 1
    s += dis(p)

print(s / cnt)