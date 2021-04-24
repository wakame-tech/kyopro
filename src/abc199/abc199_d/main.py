from itertools import groupby
from collections import deque

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ

    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]

    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def is_same(self, x, y):  # x, y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)

    def group_size(self, x):  # x が属する集合の大きさを返す
        return self.size[self.find(x)]

    def groups(self):
        return list(map(lambda k, v: list(v), groupby(range(n), key=lambda e: uf.find(e))))

# 訪れた順
def dfs(em, flags, hist, e):
    for i in range(n):
        if em[e][i] == 1 and not flags[i]:
            print(f'-> {i}', end='')
            hist.append(i)
            flags[i] = True
            flags, hist = dfs(em, flags, hist, i)
    return flags, hist

def count(em, cnt, es, idx):
    # TODO: たかだか2通り探索
    if idx == len(es):
        return cnt + 1
    for c in ['r', 'g', 'b']:
        for i in range(1, n):
            for j in range(i):
                if em[i][j] == 1:
                    cnt = count(em, cnt, es, idx + 1)
    return cnt       

# 数え上げ
def enum(n, em, grp):
    _, es = dfs(em, [False] * n, [], grp[0])
    return count(em, 0, es, grp[0])

if __name__ == "__main__":
    n, m = map(int, input().split())
    em = [[0 for _ in range(n)] for __ in range(n)]
    uf = UnionFind(n)

    for i in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        em[a][b] = em[b][a] = 1
        uf.unite(a, b)
    ans = 1
    for grp in uf.groups():
        if len(grp) == 1:
            ans *= 3
        else:
            abs *= enum(n, em, grp)

    print(ans)