from math import factorial
l = int(input())

def ncr(n, r):
  return factorial(n) // factorial(r) // factorial(n - r)

print(ncr(l - 1, 11))