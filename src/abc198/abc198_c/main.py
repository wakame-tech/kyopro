import math

r, x, y = list(map(int, input().split()))
d = math.sqrt(x ** 2 + y ** 2)
dv = math.floor(d / r)
rst = d - r * dv
if d < r:
    print(2)
else:
    print(dv + (0 if rst == .0 else 1))