n, k = list(map(int, input().split()))

fs = {}
for i in range(n):
    a, b = list(map(int, input().split()))
    if a in fs:
        fs[a] += b
    else:
        fs[a] = b

c = k
v = 0
for vi, mo in sorted(dict.items(fs), key=lambda e: e[0]):
    # ikeru
    # print(f'@{v} -> {vi}(+{mo}) cost: {vi - v} vs {c}')
    if c >= vi - v:
        c = c - (vi - v) + mo
        v = vi
    else:
        break

print(v + c)