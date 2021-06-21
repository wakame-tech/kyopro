import bisect

n, m = list(map(int, input().split()))
vs = [list(map(int, input().split())) for _ in range(m)]

v = {}
for p, y in vs:
    if p - 1 in v:
        v[p - 1].append(y)
    else:
        v[p - 1] = [y]

idxs = {}
for k, arr in dict.items(v):
    arr = list(set(arr))
    arr.sort()
    idxs[k] = arr

for i in range(m):
    idx = bisect.bisect_left(idxs[vs[i][0] - 1], vs[i][1])
    print(f'{str(vs[i][0]).rjust(6, "0")}{str(idx + 1).rjust(6, "0")}')