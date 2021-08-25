import math

n=int(input())
i = 1
while 2 ** i <= n:
    i += 1
print(i - 1)
# print(math.floor(math.log2(n)))