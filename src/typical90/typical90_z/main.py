from collections import deque
from typing import List, Tuple

def adj_list_from_edges(n: int, edges: List[Tuple[int, int]], directed: bool = False):
    """
    辺 -> 隣接頂点のリスト
    """
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u - 1].append(v - 1)
        if not directed:
            g[v - 1].append(u - 1)

    return g

n = int(input())
edges = []
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    edges.append((a, b))

def bfs(n, g):
    q = deque()
    flags = [False for _ in range(n)]
    ans = [None for _ in range(n)]
    q.append((0, True))
    ans[0] = True
    while len(q) > 0:
        u, col = q.popleft()
        ans[u] = col
        # print(f'{u}: {col}')
        for v in g[u]:
            if not flags[v]:
                flags[v] = True
                q.append((v, not col))

    # print(ans)

    col_true = [i for i in range(n) if ans[i]]
    col_false = [i for i in range(n) if not ans[i]]
    if len(col_false) >= len(col_true):
        return col_false[:n // 2]
    else:
        return col_true[:n // 2]

a = bfs(n, adj_list_from_edges(n, edges))
for i in a:
    print(i + 1, end=' ')