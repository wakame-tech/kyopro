import math
from collections import Counter
from functools import reduce

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


def ks_in_range(a: int, b: int, k: int):
    """
    count mult of k in [a, b]
    """
    r = a % k
    m = a - r
    answer = (b - m) // k + 1
    if r > 0:
        answer -= 1
    return answer


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

def num_of_divisors(n: int) -> int:
    """
    約数の個数
    """
    d = Counter(prime_factorize(n))
    res = 1
    for v in dict.values(d):
        res *= (v + 1)
    return res


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