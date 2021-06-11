from icecream import ic
import numpy as np

def is_leq_median(grid, n: int, k: int, med: int):
    """ O(N^2) """
    bit_grid = np.zeros((n, n))
    for y in range(n):
        for x in range(n):
            if med <= grid[x, y]:
                bit_grid[x, y] = 1

    cs = np.zeros((n + 1, n + 1))
    for y in range(n):
        for x in range(n):
            cs[x + 1, y + 1] = cs[x + 1, y] + cs[x, y + 1] - cs[x, y] + bit_grid[x, y]

    for y in range(n - k + 1):
        for x in range(n - k + 1):
            s, e = (x, y), (x + k, y + k)
            sm = cs[e[0], e[1]] - cs[s[0], e[1]] - cs[e[0], s[1]] + cs[s[0], s[1]]
            if sm < k ** 2 // 2 + 1:
                return False
    return True


def searach_med(grid, n: int, k: int) -> int:
    """ O(log 1^9) = O(1) """
    f, t = 0, 10 ** 9
    while f + 1 != t:
        m = (f + t) // 2
        ic(m)
        if is_leq_median(grid, n, k, m):
            f = m
        else:
            t = m

    return f


n, k = list(map(int, input().split()))
grid = []
for i in range(n):
    a = list(map(int, input().split()))
    grid.append(a)

grid = np.array(grid)

print(searach_med(grid, n, k))