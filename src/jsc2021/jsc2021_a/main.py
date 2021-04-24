import math

x, y, z =  map(int, input().split())
# y * z / x
print(math.ceil((y * z / x) - 1))