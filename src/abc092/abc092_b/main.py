import math

n = int(input())
d, x = list(map(int, input().split()))
a = [int(input()) for i in range(n)]

ans = x
for i in a:
    ans += 1 + (d - 1) // i

print(ans)