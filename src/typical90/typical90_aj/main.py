n, q = list(map(int, input().split()))
xm, ym, xM, yM = 10 ** 9, 10 ** 9, 0, 0

ps = []
for i in range(n):
    x, y = list(map(int, input().split()))
    x, y = x - y, x + y
    ps.append((x, y))
    xm = min(xm, x)
    ym = min(ym, y)
    xM = max(xM, x)
    yM = max(yM, y)

for _ in range(q):
    i = int(input())
    x, y = ps[i - 1]
    print(max(abs(x - xm), abs(y - ym), abs(x - xM), abs(y - yM)))