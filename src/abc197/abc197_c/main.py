from functools import reduce
from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

def ors(it):
    return reduce(lambda p1, p2: p1 | p2, it)

def xors(it):
    return reduce(lambda p1, p2: p1 ^ p2, it)

def split_by(l, idxs):
    res = []
    idxs = [0, *idxs, len(l)]
    for i in range(len(idxs) - 1):
        res.append(l[idxs[i]:idxs[i + 1]])
    return res

ans = 2 ** 30
if n == 1:
    print(a[0])
else:
    for k in range(1, n):
        for sps in combinations(range(1, n), k):
            listset = split_by(a, sps)
            v = xors(map(ors, listset))
            ans = min(ans, v)
    print(ans)