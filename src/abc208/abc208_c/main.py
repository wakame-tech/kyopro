import bisect

def shrink_1d(arr: list):
    """ 座標圧縮 """
    vs = list(set(arr))
    vs.sort()
    return [bisect.bisect_left(vs, e) for e in arr]

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
sh = shrink_1d(a)


for i in range(n):
    if sh[i] < k % n:
        print(k // n + 1)
    else:
        print(k // n)