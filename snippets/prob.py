from math import factorial

def ncr(n: int, r: int) -> int:
    """
    nCr
    """
    assert(n >= r)
    return factorial(n) // factorial(r) // factorial(n - r)

def npr(n: int, r: int) -> int:
    """
    nPr
    """
    assert(n >= r)
    return factorial(n) // factorial(n - r)