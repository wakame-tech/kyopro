d, n = map(int, input().split())
tmps = [int(input()) for _ in range(d)]
conds = [list(map(int, input().split())) for _ in range(n)]

def solve(tmps, conds):
    days = len(tmps)
    cloths = len(conds)
    # dp[days][cloth]: days日目にclothを着たときの絶対値
    dp = [[0 for _ in range(cloths)] for __ in range(days + 1)]

    def valid(d, i):
        return conds[i][0] <= tmps[d] <= conds[i][1]

    for d in range(1, days):
        for i in range(cloths):
            # 服 i と 服 j
            if not valid(d - 1, i):
                continue
            for j in range(cloths):
                # 着れるなら
                if not valid(d, j):
                    continue
                dlt = abs(conds[i][2] - conds[j][2])
                dp[d + 1][j] = max(dp[d + 1][j], dp[d][i] + dlt)

    return max(dp[days])

print(solve(tmps, conds))