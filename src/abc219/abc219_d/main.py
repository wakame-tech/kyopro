if __name__ == "__main__":
    inf = 10 ** 8
    n = int(input())
    x, y = list(map(int, input().split()))

    # [弁当][たこ焼き][たいやき]
    dp =[[[inf for _ in range(y + 1)] for _ in range(x + 1)] for _ in range(n + 1)]
    
    w = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        w.append((a, b))

    dp[0][0][0] = 0

    for i in range(n + 1):
        for j in range(x + 1):
            for k in range(y + 1):
                a, b = w[i - 1]
                jn, kn = min(j + a, x), min(k + b, y)
                # buy: from dp[i - 1][j][k]
                dp[i][jn][kn] = min(dp[i][jn][kn], dp[i - 1][j][k] + 1)
                # not buy
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
        
    print(-1 if dp[n][x][y] == inf else dp[n][x][y])