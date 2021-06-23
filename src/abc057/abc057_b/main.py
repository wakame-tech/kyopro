n, m = list(map(int, input().split()))

ss = []
for i in range(n):
    a, b = list(map(int, input().split()))
    ss.append((a, b))

cs = []
for i in range(m):
    c, d = list(map(int, input().split()))
    cs.append((c, d))

def solve(p, cs):
    min_i = -1
    d = 10 ** 8
    for i, c in enumerate(cs):
        dd = abs(c[0] - p[0]) + abs(c[1] - p[1])
        if dd < d:
            d = dd
            min_i = i
    return min_i

for i in range(n):
    print(solve(ss[i], cs) + 1)