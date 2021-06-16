import bisect

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


def solve(n, m, items, boxes, l, r):
    # edges(cap/cost)
    # s(@0): (1/0)
    # items_i(@1..=n)
    # boxes_i(@1+n..=1+n+m-1)
    # g(@1+n+m)
    mx = 10 ** 6
    mcf = MinCostFlow(n + m + 2)

    for i in range(1, 1 + n):
        mcf.add_edge(0, i, 1, mx - 0)

    for i in range(n):
        # print(f'w={items[i][0]}, v={items[i][1]}')
        for j in range(m):
            # (cap ? 1 : 0, mx - items_i.value)
            capable = items[i][0] <= boxes[j]
            available = not (l <= j <= r)
            # print(f'[{j}]: {capable} {available}')
            mcf.add_edge(1 + i, 1 + n + j, int(capable and available), mx - items[i][1])
    
    for i in range(1 + n, 1 + n + m):
        mcf.add_edge(i, 1 + n + m, 1, mx - 0)

    flow = m - (l - r + 1)
    mcf.flow(0, 1 + n + m, flow)

    v = 0
    for e in mcf.edges():
        if e.frm == 0 and 1 <= e.to <= n and e.cap == 0:
            # print(f'used {e.to - 1}')
            v += items[e.to - 1][1]

    return v


if __name__ == "__main__":    
    n, m, q = list(map(int, input().split()))
    items = []
    for i in range(n):
        w, v = list(map(int, input().split()))
        items.append((w, v))
    # sort by weight
    items.sort(key=lambda e: e[0])

    boxes = list(map(int, input().split()))
    for i in range(q):
        l, r = list(map(int, input().split()))
        l, r = l - 1, r - 1
        ans = solve(n, m, items, boxes, l, r)
        print(ans)