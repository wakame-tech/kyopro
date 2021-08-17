s = input()

md = 10 ** 9 + 7
dp = [0 for _ in range(len(s))]
for c in s:
    i = 'chokudai'.find(c)
    if i == 0:
        dp[0] += 1
    if i >= 1:
        dp[i] += dp[i - 1] % md

print(dp[7] % md)