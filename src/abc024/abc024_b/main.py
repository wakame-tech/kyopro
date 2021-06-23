n, d = list(map(int, input().split()))
ts = [int(input()) for _ in range(n)]

ans = 0
for i in range(len(ts) - 1):
    ans += min(d, ts[i + 1] - ts[i])
ans += d

print(ans)