from collections import defaultdict

n, k = list(map(int, input().split()))
c = list(map(int, input().split()))

d = defaultdict(int)

for i in range(k):
    d[c[i]] += 1

ans = len(d)
for i in range(n - k):
    # print(d)
    # print(f'{i}..{i + k} {ans=}')
    d[c[i + k]] += 1
    d[c[i]] -= 1
    if d[c[i]] == 0:
        del d[c[i]]
    ans = max(ans, len(d))

print(ans)