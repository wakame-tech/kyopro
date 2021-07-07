from typing import List, Tuple


class Graph:
    Inf = 10 ** 9

    @staticmethod
    def adj_mat_from_cost(n: int, costs: List[Tuple[int, int, int]], zero_indexed=False):
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


def solve(n, g):
    ans = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        # print(f'k = {k}')
        # Graph.dbg(n, g)
        for i in range(n):
            for j in range(n):
                if g[i][j] != Graph.Inf and g[i][j] != 0:
                    ans += g[i][j]
        # Graph.dbg(n, g)
    return ans


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    costs = []
    for i in range(m):
        a, b, c = list(map(int, input().split()))
        costs.append((a, b, c))

    adj = Graph.adj_mat_from_cost(n, costs)
    print(solve(n, adj))