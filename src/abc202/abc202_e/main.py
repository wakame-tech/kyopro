from collections import Counter, defaultdict

n = int(input())
(*p,) = range(n)
rank = [1] * n


def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y


def unite(x, y):
    px = root(x)
    py = root(y)
    if px == py:
        return 0
    rx = rank[px]
    ry = rank[py]
    if ry < rx:
        p[py] = px
    elif rx < ry:
        p[px] = py
    else:
        p[py] = px
        rank[px] += 1
    return 1


p = list(map(int, input().split()))
for i, pi in enumerate(p):
    unite(i, pi - 1)

q = int(input())
qs = []
for i in range(q):
    u, s = list(map(int, input().split()))

print(rank)