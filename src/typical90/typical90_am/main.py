import sys
sys.setrecursionlimit(10 ** 9)

def dfs(dp, flag, g, pos):
    dp[pos] = 1
    for i in g[pos]:
        if not flag[i]:
            flag[i] = True
            dfs(dp, flag, g, i)
            dp[pos] += dp[i]

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    # 部下の数
    dp = [0] * n
    flag = [False] * n
    flag[0] = True
    dfs(dp, flag, tree, 0)
    ans = sum(dp[i] * (n - dp[i]) for i in range(n))
    print(ans)