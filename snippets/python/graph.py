# 参考: <https://mirucacule.hatenablog.com/entry/2020/05/21/124026>
from typing import List, Tuple
from heapq import heappush, heappop

class Graph:
    Inf = 10 ** 9

    @staticmethod
    def adj_mat_from_cost(n: int, costs: List[Tuple[int, int, int]], zero_indexed = False):
        """
        コストの情報から隣接行列を作成
        n: 頂点数
        cost: (始点, 終点, 重み), 1-indexed
        """
        g = [[Graph.Inf for x in range(n)] for y in range(n)]
        for i in range(n):
            g[i][i] = 0
        for s, e, c in costs:
            if not zero_indexed:
                s -= 1
                e -= 1
            g[s][e] = c
        return g

    @staticmethod
    def dijkstra(n: int, adj: List[List[Tuple[int, int]]], s: int):
        """
        s: 始点 からの最短距離を dijkstra 法で求める
        [params]
        n: 頂点数
        adj: adj[i] 頂点 i に隣接する頂点のインデックスと重み
        s: 始点
        """
        dist = [Graph.Inf] * n
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

    @staticmethod
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

if __name__ == "__main__":
    n, m = 4, 5
    inputs = [(0, 1, 1), (0, 2, 4), (1, 2, 2), (2, 3, 1), (1, 3, 5)]
    adj = [[] for _ in range(n)]
    for s, t, c in inputs:
        adj[s].append((t, c))
    
    dist = Graph.dijkstra(n, adj, 0)
    assert(dist == [0 ,1, 3, 4])

    costs = [
        (1, 2, 3),
        (1, 4, 5),
        (2, 1, 2),
        (2, 4, 4),
        (3, 2, 1),
        (4, 3, 2),
    ]

    n = 4
    g = Graph.adj_mat_from_cost(n, costs)
    g = Graph.floyd_warshall(n, g)
    g_true = [[0, 3, 7, 5], [2, 0, 6, 4], [3, 1, 0, 5], [5, 3, 2, 0]]
    assert(g == g_true)