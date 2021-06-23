n = int(input())

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

ans = 0
for i in range(1, n + 1):
    if i % 2 == 1 and len(divisors(i)) == 8:
        ans += 1
print(ans)