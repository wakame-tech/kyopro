import math

n = int(input())
a = list(map(int, input().split()))

print(math.ceil(sum(a) / sum(e != 0 for e in a)))