import bisect

if __name__ == "__main__":
    inf = 1 << 20
    n = int(input())
    a = list(map(int, input().split()))
    # n = 8
    # a = [3, 1, 4, 1, 5, 9, 2, 6]
    p, q = [0] * n, [0] * n
    dp = [inf] * n
    # なるべく小さな昇順にしたい
    l = 0
    for i in range(n):
        # slice (dp[:l]) は遅い
        r = bisect.bisect_left(dp, a[i], hi=l)
        if r == l:
            l += 1
        dp[r] = a[i]
        p[i] = r + 1

    l = 0
    for i in reversed(range(n)):
        r = bisect.bisect_left(dp, a[i], hi=l)
        if r == l:
            l += 1
        dp[r] = a[i]
        q[i] = r + 1

    ans = max(p[i] + q[i] - 1 for i in range(n))
    print(ans)