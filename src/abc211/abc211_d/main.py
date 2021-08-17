from collections import deque
from sys import flags

md = 10 ** 9 + 7

def bfs(n, g, ans, flags, dist, s):
    q = deque()
    q.append(s)
    flags[s] = True
    dist[s] = 0
    for i in g[s]:
        ans[i] = 1

    while q:
        u = q.popleft()
        for i in g[u]:
            if not flags[i] and dist[u] + 1 < dist[i]:
                dist[i] = dist[u] + 1
                q.append(i)
                flags[i] = True
            if flags[i] and dist[i] == dist[u] + 1:
                ans[i] += ans[u] % md
        # print(g[u], ans, dist)

if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    flags = [False for _ in range(n)]
    ans = [0 for i in range(n)]
    dist = [10 ** 9 for i in range(n)]
    g = [[] for i in range(n)]

    for i in range(m):
        a, b = list(map(int, input().split()))
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    bfs(n, g, ans, flags, dist, 0)
    print(ans[n - 1] % md)