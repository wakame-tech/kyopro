n = int(input())

def npr(n: int, r: int) -> int:
    """
    nPr
    """
    assert(n >= r)
    res = 1
    for i in range(n, n - r, -1):
        res *= i
    return res


if n == 1:
    print(0)
else:
    print(((npr(n, 2) * 10 ** (n - 2))) % (10 ** 9 + 7))