import heapq
import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
g = [[] for _ in range(n)]
flags = [False for _ in range(n)]

def dfs(s):
    flags[s] = True
    print(s + 1, end=' ')

    while len(g[s]) != 0:
        nex = heapq.heappop(g[s])
        if not flags[nex]:
            dfs(nex)
            print(s + 1, end=' ')

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    heapq.heappush(g[a], b)
    heapq.heappush(g[b], a)

dfs(0)