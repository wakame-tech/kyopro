from typing import List


class LazySegtree:
    """
    遅延セグメント木
    ref: <https://algo-logic.info/segment-tree/>
    """
    def __init__(self, n: int, arr: List[int], op, e: int):
        """
        n: 区間の長さ
        arr: 要素
        op: 演算
        e: モノイド演算 op の単位元 max -> -INF, min -> INF
        """
        self.n = n
        self.op = op
        self.e = e
        self.dat = [e] * (2 * n - 1)
        for i in range(n - 1, 2 * n - 1):
            self.dat[i] = arr[i - n + 1]
        self.lazy = [e] * (2 * n - 1)

    def _print_tree(self, tree: List[int]):
        l = 1
        cnt = 0
        for e in tree:
            print(e, end=" ")
            if cnt == l - 1:
                print()
                l *= 2
            cnt += 1

    def _refresh(self, k: int):
        if self.lazy[k] == self.e:
            return
        # is not leaf
        if k < self.n - 1:
            # 子に更新を伝播
            self.lazy[k * 2 + 1] = self.lazy[k]
            self.lazy[k * 2 + 2] = self.lazy[k]

        self.dat[k] = self.lazy[k]
        self.lazy[k] = self.e

    def _update_rec(self, a: int, b: int, x: int, k: int, l: int, r: int):
        if k > self.n:
            raise Exception("update failed")

        self._refresh(k)

        if a <= l and r <= b:
            self.lazy[k] = x
            self._refresh(k)
        elif a < r and l < b:
            # left
            self._update_rec(a, b, x, k * 2 + 1, l, (l + r) // 2)
            # right
            self._update_rec(a, b, x, k * 2 + 2, (l + r) // 2, r)
            self.dat[k] = self.op(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def update(self, a: int, b: int, x: int):
        """
        [a, b) を x に更新する
        O(log N)
        """
        self._update_rec(a, b, x, 0, 0, self.n)
        # print(f'update')
        # self._print_tree(self.dat)

    def _query_rec(self, a: int, b: int, k: int, l: int, r: int):
        if k > self.n:
            raise Exception(f"query failed {k=}")

        self._refresh(k)

        # [l, r) が範囲内だったら返す
        # 遅延なし
        if r <= a or b <= l:
            return self.e
        # 完全に範囲内
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self._query_rec(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self._query_rec(a, b, k * 2 + 2, (l + r) // 2, r)
            return self.op(vl, vr)

    def query(self, a: int, b: int):
        """
        範囲 [a, b) に対して op をする
        O(log N)
        """
        assert a >= 0 and b < self.n
        res = self._query_rec(a, b, 0, 0, self.n)
        # print(f'query')
        # self._print_tree(self.dat)
        return res


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

    def set(self, p: int, x: int):
        # 一点更新
        assert 0 <= p < self.n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def get(self, p: int) -> int:
        # 一点取得
        assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def query(self, l: int, r: int) -> int:
        assert 0 <= l <= r and r <= self.n
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
    w, n = 100, 4
    w = 8
    qs = [(2, 7), (0, 3), (5, 6), (1, 4)]
    segtree = LazySegtree(w, [0] * w, max, 0)
    for l, r in qs:
        mx = segtree.query(l, r + 1)
        print(f"[l, r) = [{l}, {r + 1}) max = {mx}")
        segtree.update(l, r + 1, mx + 1)
        print(segtree.query(l, r))