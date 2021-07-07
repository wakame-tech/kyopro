import bisect


def shrink_1d(arr: list):
    """ 座標圧縮 """
    vs = list(set(arr))
    vs.sort()
    return [bisect.bisect_left(vs, e) for e in arr]


n = int(input())
a = [int(input()) for _ in range(n)]

s = shrink_1d(a)
for i in s:
    print(i)