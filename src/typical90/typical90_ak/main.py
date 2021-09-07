from typing import List

class Segtree:
    def __init__(self, arr: List[int], op, e: int):
        # 構築
        self.n = len(arr)
        self.op = op
        self.e = e
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def query(self, l: int, r: int) -> int:
        """
        RMQ
        """
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                smr = self.op(self.d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

if __name__ == "__main__":
    w, n = list(map(int, input().split()))
    rs = []
    for i in range(n):
        l, r, v = list(map(int, input().split()))
        rs.append((l, r, v))

    dp = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        l, r, v = rs[i]
        segtree = Segtree(dp[i], max, -1)
        for j in range(w + 1):
            # 範囲 [j - r, j - l]
            mx = segtree.query(max(0, j - r), j - l + 1)
            if j < l or mx < 0: # 選べない
                dp[i + 1][j] = dp[i][j]
            else: # 選ぶ
                dp[i + 1][j] = max(dp[i][j], mx + v)

    print(dp[n][w])