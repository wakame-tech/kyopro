# 参考: <https://mirucacule.hatenablog.com/entry/2020/05/21/124026>
from typing import List, Tuple, Union
from heapq import heappush, heappop
from collections import deque

Inf = 10 ** 9


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


def adj_mat_from_cost(n: int, costs: List[Tuple[int, int, int]], zero_indexed=False):
    """
    コストの情報から隣接行列を作成
    n: 頂点数
    cost: (始点, 終点, 重み), 1-indexed
    """
    g = [[Inf for x in range(n)] for y in range(n)]
    for i in range(n):
        g[i][i] = 0
    for s, e, c in costs:
        if not zero_indexed:
            s -= 1
            e -= 1
        g[s][e] = c
    return g


def dijkstra(n: int, adj: List[List[Tuple[int, int]]], s: int):
    """
    s: 始点 からの最短距離を dijkstra 法で求める
    [params]
    n: 頂点数
    adj: adj[i] 頂点 i に隣接する頂点のインデックスと重み
    s: 始点
    """
    dist = [Inf] * n
    # (distance, node)
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n

    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))

    return dist


def floyd_warshall(n: int, g: List[List[int]]):
    """
    floyd_warshall法
    n: 頂点数
    g: 隣接行列
    """
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    return g


def scc(n: int, edges: List[Tuple[int, int]]):
    """
    強連結成分分解
    <https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html>
    <https://www.slideshare.net/hcpc_hokudai/study-20150107>
    <https://pione.hatenablog.com/entry/2021/03/11/232159>
    """
    import sys
    sys.setrecursionlimit(10 ** 7)

    g = adj_list_from_edges(n, edges, True)
    g_t = adj_list_from_edges(n, [(t, f) for f, t in edges], True)

    order = []
    visited = [False] * n
    group_indice: List[Union[int, None]] = [None] * n

    def dfs(s: int):
        visited[s] = True
        for t in g[s]:
            if not visited[t]:
                dfs(t)
        order.append(s)

    def rdfs(s: int, cnt: int):
        group_indice[s] = cnt
        visited[s] = True
        for t in g_t[s]:
            if not visited[t]:
                rdfs(t, cnt)

    # step 1. 帰りがけ順に順番を記録
    for i in range(n):
        if not visited[i]:
            dfs(i)

    visited = [0] * n
    cnt = 0

    # step 2. 後に記録した頂点からDFS
    for s in reversed(order):
        if not visited[s]:
            rdfs(s, cnt)
            cnt += 1

    return cnt, group_indice


def diameter(n: int, g: List[List[int]]):
    """
    木の直径
    """

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
    return bfs(n, g, i)[1]


def topological_sort(n: int, edges: List[Tuple[int, int]]):
    """
    DAGに対してトポロジカルソートを行う
    """
    from collections import defaultdict

    indegs = defaultdict(lambda: 0)
    outs = defaultdict(lambda: [])
    for f, t in edges:
        indegs[t - 1] += 1
        outs[f - 1].append(t - 1)

    res = []
    q = deque([i for i in range(n) if indegs[i] == 0])
    while q:
        u = q.popleft()
        res.append(u)
        for v in outs[u]:
            indegs[v] -= 1
            if indegs[v] == 0:
                q.append(v)

    return res


def _test_dijkstra():
    n, m = 4, 5
    inputs = [(0, 1, 1), (0, 2, 4), (1, 2, 2), (2, 3, 1), (1, 3, 5)]
    adj = [[] for _ in range(n)]
    for s, t, c in inputs:
        adj[s].append((t, c))

    dist = dijkstra(n, adj, 0)
    assert dist == [0, 1, 3, 4]


def _test_floyd_warshall():
    costs = [
        (1, 2, 3),
        (1, 4, 5),
        (2, 1, 2),
        (2, 4, 4),
        (3, 2, 1),
        (4, 3, 2),
    ]

    n = 4
    g = adj_mat_from_cost(n, costs)
    g = floyd_warshall(n, g)
    g_true = [[0, 3, 7, 5], [2, 0, 6, 4], [3, 1, 0, 5], [5, 3, 2, 0]]
    assert g == g_true


def _test_scc():
    n = 9
    edges = [
        (1, 2),
        (2, 7),
        (7, 1),
        (4, 2),
        (5, 4),
        (9, 5),
        (6, 9),
        (4, 6),
        (6, 8),
        (8, 3),
        (3, 8),
    ]
    _, groups = scc(n, edges)
    assert groups == [2, 2, 1, 0, 0, 0, 2, 1, 0]


def _test_diameter():
    n = 5
    edges = [
        (1, 2),
        (2, 3),
        (3, 4),
        (3, 5),
    ]
    g = adj_list_from_edges(n, edges)
    assert diameter(n, g) == 3


if __name__ == "__main__":
    _test_dijkstra()
    _test_floyd_warshall()
    _test_scc()
    _test_diameter()