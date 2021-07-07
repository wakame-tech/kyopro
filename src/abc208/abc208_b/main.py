import math

p = int(input())
ans = 0

for i in range(10, 0, -1):
    j = 0
    while True:
        if math.factorial(i) * j > p:
            break
        j += 1
    p -= math.factorial(i) * (j - 1)
    ans += (j - 1)

print(ans)