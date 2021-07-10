# TODO: submit
from collections import deque

def bfs(n, d, s, dist):
    q = deque()
    q.append((s, 0))
    flags = [False for _ in range(n)]
    flags[s] = True
    cnt = 0
    while len(q) != 0:
        p, _dist = q.pop()
        if _dist == dist:
            cnt += 1
            continue
        for i in range(n):
            if not flags[i] and d[p][i] == 1:
                flags[i] = True
                q.append((i, _dist + 1))

    return cnt

n, m = list(map(int, input().split()))
d = [[0 for x in range(n)] for y in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    d[a][b] = d[b][a] = 1

for i in range(n):
    cnt = bfs(n, d, i, 2)
    print(cnt)