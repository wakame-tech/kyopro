# TODO: submit
from collections import defaultdict

n = int(input())
d = defaultdict(lambda: 0)
for i in range(n):
    a, b = list(map(int, input().split()))
    d[a] += 1
    d[b + 1] += -1

ans = 0
cs = 0
for k, v in sorted(d.items(), key=lambda e: e[0]):
    cs += v
    ans = max(ans, cs)

print(ans)