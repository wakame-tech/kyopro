import bisect

def shrink_1d(arr: list):
    """ 座標圧縮 """
    vs = list(set(arr))
    vs.sort()
    return [bisect.bisect_left(vs, e) for e in arr]

h,w,n=list(map(int, input().split()))
xs, ys = [], []
for i in range(n):
    a,b=list(map(int, input().split()))
    xs.append(b)
    ys.append(a)

xsi = shrink_1d(xs)
ysi = shrink_1d(ys)

for i in range(n):
    print(ysi[i] + 1, xsi[i] + 1)