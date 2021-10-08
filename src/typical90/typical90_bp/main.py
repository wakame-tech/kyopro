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


if __name__ == "__main__":
    n = int(input())
    q = int(input())
    qs = []
    for i in range(q):
        t, x, y, v = map(int, input().split())
        qs.append((t, x - 1, y - 1, v))

    # 和
    weights = [0] * n
    for t, x, y, v in qs:
        weights[x] = v

    print(weights)

    uf = UnionFind(n)
    for i, (t, x, y, v) in enumerate(qs):
        if t == 0:
            uf.union(x, y)
        else:
            if not uf.same(x, y):
                print(f'Ambiguous')
            else:
                # TODO: やれ
                print(weights)