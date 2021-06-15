# 参考: <https://tjkendev.github.io/procon-library/python/min_cost_flow/primal-dual.html>
# from dataclasses import dataclass
from typing import List
from heapq import heappush, heappop

# @dataclass
class Edge:
    # frm: int
    # to: int
    # cap: int
    # cost: int
    # rev: object # Edge?

    def __init__(self, frm: int, to: int, cap: int, cost: int, rev: object):
        self.frm = frm
        self.to = to
        self.cap = cap
        self.cost = cost
        self.rev = rev

    def __repr__(self):
        return f'{self.frm}->{self.to} cap/cost {self.cap}/{self.cost}'

class MinCostFlow:
    def __init__(self, n: int):
        self.n = n
        self.inf = 10 ** 18
        self.g: List[List[Edge]] = [[] for i in range(n)]

    def add_edge(self, frm: int, to: int, cap: int, cost: int):
        fwd = Edge(frm, to, cap, cost, None)
        bwd = Edge(to, frm, 0, -cost, fwd)
        fwd.rev = bwd
        self.g[frm].append(fwd)
        self.g[to].append(bwd)

    def edges(self):
        es = []
        for e in self.g:
            es.extend(e)
        return es

    def flow(self, s: int, t: int, f: int):
        """ flow from s to t, amount=f """
        res = 0
        h = [0] * self.n
        prv_v = [0] * self.n
        prv_e: List[Edge] = [None] * self.n
        d0 = [self.inf] * self.n
        dist = [self.inf] * self.n

        while f:
            dist[:] = d0
            dist[s] = 0
            # (cost, value)[]
            que = [(0, s)]
            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + h[v]
                for e in self.g[v]:
                    if e.cap > 0 and r0 + e.cost - h[e.to] < dist[e.to]:
                        dist[e.to] = r =  r0 + e.cost - h[e.to]
                        prv_v[e.to] = v
                        prv_e[e.to] = e
                        heappush(que, (r, e.to))

            if dist[t] == self.inf:
                return None
            
            for i in range(self.n):
                h[i] += dist[i]
            
            d, v = f, t
            while v != s:
                d = min(d, prv_e[v].cap)
                v = prv_v[v]
            f -= d
            res += d * h[t]
            v = t
            while v != s:
                e = prv_e[v]
                e.cap -= d
                e.rev.cap += d
                v = prv_v[v]

        return res


if __name__ == '__main__':
    # <https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=jp>
    n, m, f = 4, 5, 2
    qs = [
        # from, to, cap, cost
        [0, 1, 2, 1],
        [0, 2, 1, 2],
        [1, 2, 1, 1],
        [1, 3, 1, 3],
        [2, 3, 2, 1],
    ]
    mcf = MinCostFlow(n)
    for i in range(m):
        frm, to, cap, cost = qs[i]
        mcf.add_edge(frm, to, cap, cost)
    
    res = mcf.flow(0, n - 1, f)
    assert(res == 6)

    for e in mcf.edges():
        print(e)