# 参考: <https://mirucacule.hatenablog.com/entry/2020/05/21/124026>
from typing import List, Tuple
from heapq import heappush, heappop

class Graph:
    Inf = 10 ** 9

    @staticmethod
    def adj_list_from_directed_edge(n: int, edges: List[Tuple[int, int]]):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u - 1].append(v - 1)
        return g

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

    @staticmethod
    def scc(n: int, edges: List[Tuple[int, int]]):
        """
        強連結成分分解
        <https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html>
        <https://www.slideshare.net/hcpc_hokudai/study-20150107>
        <https://pione.hatenablog.com/entry/2021/03/11/232159>
        """
        label = { i: -1 for i in range(n) }

        def dfs(s: int):
            # print(s)
            for i in adj[s]:
                if not dfs.visited[i]:
                    dfs.visited[i] = True
                    dfs(i)

                    label[i] = dfs.cnt
                    dfs.cnt += 1

        dfs.cnt = 0
        dfs.visited = [False] * n

        def dfs2(s: int):
            dfs2.ans.append(s)
            for i in inv_adj[s]:
                if not dfs2.visited[i]:
                    dfs2.visited[i] = True
                    dfs2(i)

        dfs2.visited = [False] * n

        # ステップ1: 帰りがけ順に番号ふる
        adj = Graph.adj_list_from_directed_edge(n, edges)
        for i in range(n):
            if dfs.visited[i]:
                continue

            dfs.visited[i] = True
            dfs(i)
            label[i] = dfs.cnt
            dfs.cnt += 1

        # ステップ2: 番号大きい順にDFS
        inv_edges = [(t, f) for f, t in edges]
        inv_adj = Graph.adj_list_from_directed_edge(n, inv_edges)
        label_swap = { v: k for k, v in label.items() }
        ans = []
        for i in reversed(range(n)):
            if i not in dict.keys(label_swap):
                continue
            v = label_swap[i]
            if dfs2.visited[v]:
                continue
            dfs2.ans = []
            dfs2.visited[v] = True
            dfs2(v)
            ans.append(dfs2.ans)
        
        return ans


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
        (3, 8)
    ]

    assert(Graph.scc(n, edges) == [[3, 4, 8, 5], [2, 7], [0, 6, 1]])
