import bisect

def shrink_1d(arr: list):
    """ 座標圧縮 """
    vs = list(set(arr))
    vs.sort()
    return [bisect.bisect_left(vs, e) for e in arr]