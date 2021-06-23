n=int(input())
vs = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    vs.append((s, p))

s = sum(map(lambda e: e[1], vs))
si = max(vs, key=lambda e: e[1])
print(si[0] if si[1] > s // 2 else 'atcoder')