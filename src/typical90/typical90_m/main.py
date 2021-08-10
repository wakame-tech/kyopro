from typing import List, Tuple
from heapq import heappush, heappop


class Graph:
    Inf = 10 ** 9

    @staticmethod
    def adj_list_from_cost(n: int, costs: List[Tuple[int, int, int]]):
        g = [[] for _ in range(n)]
        for u, v, c in costs:
            g[u - 1].append((v - 1, c))
            g[v - 1].append((u - 1, c))
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


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = []
    for i in range(m):
        a, b, c = list(map(int, input().split()))
        s.append((a, b, c))
    
    adj = Graph.adj_list_from_cost(n, s)

    ans = Graph.dijkstra(n, adj, 0)
    ans2 = Graph.dijkstra(n, adj, n - 1)
    for i, j in zip(ans, ans2):
        print(i + j)