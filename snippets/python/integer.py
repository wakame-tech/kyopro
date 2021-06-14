import math
from functools import reduce
from collections import Counter

def divisors(n: int) -> list:
    """
    nの約数
    """
    res = []
    for q in range(1, int(math.sqrt(n)) + 1):
        if n % q == 0:
            res.append(n // q)
            if q < n // q:
                res.append(q)
    
    return res

def prime_factorize(n: int) -> list:
    """
    素因数分解
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def lcm(x: int, y: int) -> int:
    """
    最小公倍数
    """
    return (x * y) // math.gcd(x, y)

def gcds(arr: list) -> int:
    """
    multi gcd
    """
    return reduce(math.gcd, arr)

def lcms(arr: list) -> int:
    return reduce(lcm, arr, 1)