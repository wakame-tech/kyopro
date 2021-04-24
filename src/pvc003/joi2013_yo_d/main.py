d, n = map(int, input().split())
t = []
for i in range(d):
    t.append(int(input()))

cond = []
for i in range(n):
    a, b, c = map(int, input().split())
    cond.append((a, b, c))

def dbg(dp):
    for i in range(d + 1):
        print(dp[i])

dp = [[0 for _ in range(n)] for __ in range(d + 1)]

for k in range(n):
    if cond[k][0] <= t[0] <= cond[k][1]:
        dp[0][k] = cond[k][2]

for i in range(1, d + 1):
    for j in range(n):
        m = 0
        for k in range(n):
            if cond[k][0] <= t[i] <= cond[k][1]:
                m = max(m, dp[i][j] + abs(dp[i][j] - cond[k][2]))
        dp[i + 1][j] = m

# dbg(dp)

print(max(dp[d - 1]))