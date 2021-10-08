n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

inf = 10 ** 9
dp = [inf for _ in range(n + 1)]

mx = inf
for i in range(n):
    if mx < t[i]:
        mx = t[i]
    dp[i] = mx
    mx += s[i]
