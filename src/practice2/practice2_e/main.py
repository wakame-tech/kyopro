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

def solve(n, k, a):
    mx = 10 ** 9
    # [0]: s
    # [1..n]: lines
    # [n+1..2n]: rows
    # [2n+1]: g
    mcf = MinCostFlow(1 + n + n + 1)
    si, gi = 0, 2 * n + 1

    # skip
    mcf.add_edge(si, gi, mcf.inf, mx - 0)

    for i in range(n):
        # s(@si=0) -> lines(@1 + i)
        mcf.add_edge(si, 1 + i, k, 0)
        # rows(@n + i + 1) -> g(@1 + n + n)
        mcf.add_edge(1 + n + i, gi, k, 0)
    
    # cell
    # line(@1 + i)
    for i in range(n):
        # row(1 + n + j)
        for j in range(n):
            mcf.add_edge(1 + i, 1 + n + j, 1, mx - a[i][j])

    def is_cell(e):
        return 1 <= e.frm <= n and n + 1 <= e.to <= 2 * n
    
    mcf.flow(si, gi, n * k)

    ans = [['.' for x in range(n)] for y in range(n)]
    sm = 0
    for e in mcf.edges():
        # cap != 0 means 'unused'
        if not is_cell(e) or e.cap != 0:
            continue
        # print(e, e.frm - 1, e.to - n - 1)
        ans[e.frm - 1][e.to - n - 1] = 'X'
        sm += mx - e.cost

    return sm, ans

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    sm, ans = solve(n, k, a)
    print(sm)
    for i in range(n):
        print(*ans[i], sep='')