from itertools import groupby

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        # 親
        self.parent = [i for i in range(n)]
        # 木の高さ
        self.rank = [1] * n
        # size[i] は i を根とするグループのサイズ
        self.size = [1] * n

    def find(self, x: int) -> int:
        """
        x の根を返す
        """
        if self.parent[x] == x:
            return x
        else:
            # 経路圧縮
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x: int, y: int):
        """
        x, y の属する集合を併合する
        """
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

    def is_same(self, x: int, y: int) -> bool:
        """
        x, y が同じ集合に属するか判定する
        """
        return self.find(x) == self.find(y)

    def group_size(self, x: int) -> int:
        """
        x が属する集合の大きさを返す
        """
        return self.size[self.find(x)]

    def groups(self) -> list:
        """
        各グループを返す
        """
        grps =  groupby(range(self.n), key=lambda e: self.find(e))
        res = []
        for k, v in grps:
            res.append(list(v))
        return res