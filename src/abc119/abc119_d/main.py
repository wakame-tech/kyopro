import bisect
from itertools import product

inf = 10 ** 18
a, b, q = list(map(int, input().split()))
s = list(sorted([-inf] + [int(input()) for _ in range(a)] + [inf]))
t = list(sorted([-inf] + [int(input()) for _ in range(b)] + [inf]))

def lr(xs, x):
    # left and right of x in xs
    i = bisect.bisect_left(xs, x)
    return xs[max(0, i - 1)], xs[min(len(xs) - 1, i)]

def dist(x, q):
    # distance of x -> x2 -> x3
    x2 = lr(s if q[0] else t, x)[q[1]]
    x3 = lr(t if q[0] else s, x2)[q[2]]
    return abs(x2 - x) + abs(x3 - x2)

for i in range(q):
    x = int(input())
    # [0: 先神社に行く, 1: 先寺に行く], [0: 左, 1: 右], [0: 左, 1: 右] の直積
    print(min([dist(x, q) for q in product([0, 1], repeat=3)]))