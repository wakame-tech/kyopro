import math
from collections import Counter

def prime_factorize(n: int) -> list:
    """
    素因数分解
    """
    assert(n != 0)
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

n = int(input())
fac = {}
for i in range(1, n + 1):
    d = Counter(prime_factorize(i))
    for k, v in dict.items(d):
        if k in fac:
            fac[k] += v
        else:
            fac[k] = v

if 1 in fac:
    del fac[1]

# print(fac)

ans = 1
for v in dict.values(fac):
    ans *= (v + 1)

print(ans % (10 ** 9 + 7))