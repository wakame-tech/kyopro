n, d, h = map(int, input().split())
m = 0
for i in range(n):
    di, hi = map(int, input().split())
    l = (h - hi) / (d - di)
    y = -d * l + h
    y = max(0, y)
    m = max(m, y)

print(m)