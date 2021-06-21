# 14:16-14:37
from collections import Counter
import math

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

def sum_n(s: int):
    # sum n = s <=> s = (-1 + sqrt(1 + 8s)) / 2
    return int((-1 + math.sqrt(1 + 8 * s)) / 2)

n = int(input())
pows = Counter(prime_factorize(n)).values()
print(sum(sum_n(p) for p in pows))