k = int(input())
md = 10 ** 9 + 7
dp = [0] * (k + 1)
dp[0] = 1

if k % 9 != 0:
    print(0)
else:
    for i in range(1, k + 1):
        # S(i) = sum_{1..9} S(i - j)
        for j in range(1, min(i, 9) + 1):
            dp[i] += dp[i - j] % md

    print(dp[k] % md)