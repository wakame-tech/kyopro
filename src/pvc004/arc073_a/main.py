n, t = map(int, input().split())
ts = list(map(int, input().split()))
ts.append(ts[-1] + t)
ds = []
ans = 0
for i in range(n):
    ans += min(t, ts[i + 1] - ts[i])

print(ans)