import math

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

n = int(input())
ans = 0
for dv in divisors(2 * n):
    e, l = 2 * n // dv, dv
    if (e + l) % 2 == 1:
        ans += 1
print(ans)