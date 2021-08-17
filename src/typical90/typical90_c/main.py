from collections import deque

n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)


def bfs(n, g, s):
    dist = [10 ** 6 for _ in range(n)]
    flags = [False for _ in range(n)]
    q = deque()
    q.append(s)
    dist[s] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if not flags[v] and dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                flags[v] = True
                q.append(v)
    return max(enumerate(dist), key=lambda x: x[1])


i = bfs(n, g, 0)[0]
r = bfs(n, g, i)[1]
print(r + 1)