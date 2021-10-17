

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

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    r = 5000
    mp = [[0 for i in range(r)] for j in range(r)]
    for i in range(n):
        a, b = list(map(int, input().split()))
        mp[a - 1][b - 1] = 1
    c = CumSum2D(mp)

    ans = 0
    for a in range(k, r):
        for b in range(k, r):
            ans = max(ans, c.sum((a - k - 1, b - k - 1), (a, b)))

    print(ans)
