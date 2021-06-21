from collections import defaultdict

class UnionFind():
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

    def member(self, x: int):
        ms = []
        for i in range(self.n):
            if self.same(x, i):
                ms.append(i)
        return ms

    def all_group_members(self) -> dict:
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def solve(n, a):
    uf = UnionFind(2 * 10 ** 5)
    for i in range(n // 2):
        if a[i] != a[n - 1 - i]:
            # print(f'{a[i]} -> {a[n - i - 1]}')
            uf.union(a[i] - 1, a[n - i - 1] - 1)
    
    roots = uf.roots()
    mx = 0
    for root in roots:
        # if uf.size(root) > 1:
        #     print(uf.member(root))

        if uf.size(root) >= 2:
            mx += uf.size(root) - 1

    return mx

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))