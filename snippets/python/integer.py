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


def eratosthenes(n: int):
    """
    2..N までの素因数の種類数を記録する
    O(n log log n)
    """
    c = [0] * (n + 1)
    for i in range(2, n + 1):
        if c[i] == 0:
            for j in range(i, n + 1, i):
                c[j] += 1
    return c


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

def base_10_to_k(x: int, k: int, ecd = int) -> list:
    if x // k != 0:
        return [*base_10_to_k(int(x / k), k, ecd), ecd(x % k)]
    return [ecd(x % k)]

def base_k_to_10(x, k: int, dcd = int) -> int:
    out = 0
    for i in range(1, len(x) + 1):
        out += dcd(x[-i]) * (k ** (i - 1))
    return out

def test_base_10_to_k():
    assert(base_10_to_k(10, 2) == [1, 0, 1, 0])
    assert(base_10_to_k(10, 2) == [1, 0, 1, 0])
    to_hex = lambda e: str(e) if 0 <= e < 10 else chr(ord('a') + (e - 10))
    assert(base_10_to_k(17, 16, to_hex) == ['1', '1'])

    print(base_k_to_10('ff', 16, lambda e: int(f'0x{e}', 0)))
    assert(base_k_to_10('1111', 2) == 15)

if __name__ == "__main__":
    test_base_10_to_k()