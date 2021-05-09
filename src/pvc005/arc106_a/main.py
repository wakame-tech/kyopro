import math

n = int(input())
m = 10 ** 18
f = False

for a in range(1, int(math.log(m, 3)) + 1):
    for b in range(1, int(math.log(m, 5)) + 1):
        if not f and 3 ** a + 5 ** b == n:
            print(a, b)
            f = True
if not f:
    print(-1)