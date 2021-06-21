s = int(input())
M = 10 ** 9 + 7

dp = [0] * 2001
dp[0] = 1

for i in range(3, 2001):
    dp[i] = sum(dp[j] for j in range(i - 2)) % M

print(dp[s])