import bisect

def solve(n, t):
    """
    O(n s), n = 10^2, s = 10^5
    """
    s = sum(t)
    dp = [[False for x in range(s + 1)] for y in range(n)]
    for i in [0, t[0]]:
        dp[0][i] = True

    for i in range(1, n):
        for k in range(s + 1):
            if dp[i - 1][k]:
                dp[i][k] = True
                dp[i][k + t[i]] = True
        
    ps = [j for j in range(s + 1) if dp[-1][j]]
    li = bisect.bisect_left(ps, s // 2)
    o1 = ps[li]
    return max(o1, s - o1)

if __name__ == "__main__":
    n = int(input())
    t = list(map(int, input().split()))

    ans = solve(n, t)
    print(ans)