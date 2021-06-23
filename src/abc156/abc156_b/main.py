import math

n, k = list(map(int, input().split()))
print(int(math.log(n, k)) + 1)