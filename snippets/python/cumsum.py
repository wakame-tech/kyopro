
# 1D cumsum
class CumSum1D:
    def __init__(self, arr: list):
        self.s = [0]
        l = len(arr)
        for i in range(l):
            self.s.append(self.s[i] + arr[i])

    def sum(self, s: int, e: int) -> int:
        """ [s, e) """
        return self.s[e] - self.s[s]

# 2D cumsum
class CumSum2D:
    def __init__(self, grid: list) -> None:
        w, h = len(grid[0]), len(grid)
        self.s = [[0 for i in range(w + 1)] for j in range(h + 1)]
        for i in range(h):
            for j in range(w):
                self.s[i + 1][j + 1] = self.s[i][j + 1] + self.s[i + 1][j] - self.s[i][j] + grid[i][j]

    def sum(self, s: tuple, e: tuple) -> int:
        """ [sx, ex) * [sy, ey) """
        return self.s[e[0]][e[1]] - self.s[s[0]][e[1]] - self.s[e[0]][s[1]] + self.s[s[0]][s[1]]

def test_cumsum():
    cs1 = CumSum1D([1, 3, 4, 2, 5])
    assert(cs1.sum(2, 4) == 6)
    assert(cs1.sum(0, 5) == 15)

    cs2 = CumSum2D([
        [1, 8, 7, 3, 2],
        [9, 1, 3, 4, 6],
        [3, 5, 8, 1, 4],
        [2, 7, 3, 2, 5]
    ])
    assert(cs2.sum((1, 2), (3, 5)) == 26)
    assert(cs2.sum((0, 1), (2, 3)) == 19)
    assert(cs2.sum((0, 0), (4, 5)) == 84)

test_cumsum()
