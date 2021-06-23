import math
a, b, k = list(map(int, input().split()))
g = math.gcd(a, b)

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

ds = divisors(g)
ds.sort()
print(ds[-k])