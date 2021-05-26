import math
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

def gcds(arr: list) -> int:
    """
    multi gcd
    """
    return reduce(math.gcd, arr)

print(gcds(a))