from collections import defaultdict


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int):
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x: int) -> list:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list:
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self) -> dict:
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


h, w = list(map(int, input().split()))


def to_index(x, y):
    return y * w + x


g = [[0 for x in range(w)] for y in range(h)]
Q = int(input())
uf = UnionFind(h * w)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        p = (q[2] - 1, q[1] - 1)
        g[p[1]][p[0]] = 1
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                p[0] + d[0] < 0
                or p[0] + d[0] >= w
                or p[1] + d[1] < 0
                or p[1] + d[1] >= h
            ):
                continue
            if g[p[1] + d[1]][p[0] + d[0]] == 1:
                uf.union(to_index(p[0] + d[0], p[1] + d[1]), to_index(*p))
    else:
        p1, p2 = (q[2] - 1, q[1] - 1), (q[4] - 1, q[3] - 1)
        if g[p1[1]][p1[0]] != 1 or g[p2[1]][p2[0]] != 1:
            print("No")
        else:
            print("Yes" if uf.same(to_index(*p1), to_index(*p2)) else "No")
