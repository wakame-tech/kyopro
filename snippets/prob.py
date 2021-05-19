def ncr(n: int, r: int) -> int:
    """
    nCr
    """
    assert(n >= r)
    res = 1
    for i in range(n, n - r, -1):
        res *= i
    for i in range(r, 0, -1):
        res //= i
    return res
    # return factorial(n) // factorial(r) // factorial(n - r)

def npr(n: int, r: int) -> int:
    """
    nPr
    """
    assert(n >= r)
    res = 1
    for i in range(n, n - r, -1):
        res *= i
    return res
    # return factorial(n) // factorial(n - r)