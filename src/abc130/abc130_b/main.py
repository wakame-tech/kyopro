import bisect

n, x = list(map(int, input().split()))
l = list(map(int, input().split()))


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

cs = CumSum1D(l)
print(bisect.bisect_right(cs.s, x))