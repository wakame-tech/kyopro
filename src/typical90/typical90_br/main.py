import statistics

n = int(input())
xs, ys = [], []
for i in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

def m_d(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

xc, yc = statistics.median(xs), statistics.median(ys)
print(int(sum(m_d(x, y, xc, yc) for x, y in zip(xs, ys))))