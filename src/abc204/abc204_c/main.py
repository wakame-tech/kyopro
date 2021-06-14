import sys
import random
sys.setrecursionlimit(10 ** 4)

def dfs(n, s):
    if flags[s]:
        return

    flags[s] = True
    for i in d[s]:
        dfs(n, i)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    d = [[] for x in range(n)]
    for i in range(m):
        a, b = list(map(int, input().split()))
        a, b = a - 1, b - 1
        d[a].append(b)

    # n, m = 2000, 10000
    # d = [[] for i in range(n)]
    # for i in range(m):
    #     d[random.randint(0, n - 1)].append(random.randint(0, n - 1))
    
    ans = 0
    for s in range(n):
        flags = [False] * n
        dfs(n, s)
        ans += sum(flags)

    print(ans)