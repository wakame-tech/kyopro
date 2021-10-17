import heapq
from typing import List, Tuple
from collections import defaultdict

def topological_sort(n: int, edges: List[Tuple[int, int]]):
    """
    DAGに対してトポロジカルソートを行う
    """
    indegs = defaultdict(lambda: 0)
    outs = defaultdict(lambda: [])
    for f, t in edges:
        indegs[t] += 1
        heapq.heappush(outs[f], t)

    res = []
    q = [i for i in range(n) if indegs[i] == 0]
    heapq.heapify(q)
    while q:
        u = heapq.heappop(q)
        res.append(u)
        for v in outs[u]:
            indegs[v] -= 1
            if indegs[v] == 0:
                heapq.heappush(q, v)

    return res

if __name__ == "__main__":
    n,m = list(map(int, input().split()))
    edges = []
    for i in range(m):
        a, b = list(map(int, input().split()))
        edges.append((a - 1, b - 1))

    tps = topological_sort(n, edges)

    # has cycle ?
    if len(tps) != n:
        print(-1)
    else:
        print(*map(lambda e: e + 1, tps), sep=' ')