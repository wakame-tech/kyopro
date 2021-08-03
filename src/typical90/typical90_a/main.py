def debug(func):
    def inner(*args):
        res = func(*args)
        print(f'[@debug] {func.__name__}{args} = {res}')
        return res
    return inner

# @debug
def is_ok(n: int, a: list, l: int, p: int, k: int):
    _pre = 0
    min_l = 10 ** 9
    for i in range(n):
        if p <= a[i] - _pre:
            min_l = min(min_l, a[i] - _pre)
            _pre = a[i]
            k -= 1
        if k == 0:
            min_l = min(min_l, l - _pre)
            return l - _pre >= p, min_l

    return False, min_l


def binary_search(n: int, a: list, l: int, k: int):
    """ 二分探索 """
    left = 0
    right = 10 ** 9 + 1
    score = 0

    while right - left > 1:
        mid = left + (right - left) // 2

        ok, ans = is_ok(n, a, l, mid, k)
        if ok:
            score = max(score, ans)
            left = mid
        else:
            right = mid

    return score


if __name__ == "__main__":
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))
    print(binary_search(n, a, l, k))
