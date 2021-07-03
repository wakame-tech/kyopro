def dis_m(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

n, m = list(map(int, input().split()))

ss = []
for i in range(n):
    a, b = list(map(int, input().split()))
    ss.append((a, b))

cs = []
for i in range(m):
    c, d = list(map(int, input().split()))
    cs.append((c, d))

def solve(m, p, cs):
    return min(range(m), key=lambda i: dis_m(p, cs[i]))

for i in range(n):
    print(solve(m, ss[i], cs) + 1)