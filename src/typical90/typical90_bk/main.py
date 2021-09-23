from itertools import combinations
from collections import Counter

h, w = list(map(int, input().split()))
p = []
for i in range(h):
    p.append(list(map(int, input().split())))

def row_same(p, rows):
    r = []
    for i in range(w):
        if all(p[rows[0]][i] == p[j][i] for j in rows):
            r.append(p[rows[0]][i])
    return r

ans = 0
for a in range(1, h + 1):
    for rows in combinations(range(h), a):
        rows = list(rows)
        r = row_same(p, rows)
        # print([p[j] for j in rows], r)
        cntr = Counter(r).most_common()
        d = 0 if len(cntr) == 0 else cntr[0][1]
        ans = max(ans, d * a)
        # print(f"{a=} {rows=} {d=}")

print(ans)