import math

n = int(input())

def divisors(n):
    res = []
    for q in range(1, int(math.sqrt(n)) + 1):
        if n % q == 0:
            res.append(n // q)
            if q < n // q:
                res.append(q)
    
    return res

for i in sorted(divisors(n)):
    print(i)