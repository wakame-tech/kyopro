import math

a, b = list(map(int, input().split()))

i = 0
ans = 0
while True:
    i += a
    ans += 1
    if i >= b:
        break
    i -= 1
print(ans)