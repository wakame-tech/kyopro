n, ps = int(input()), [(0, 0, 0)]

def f(x1, y1, x2, y2, t):
    d = abs(x1 - x2) + abs(y1 - y2)
    return t >= d and (d + t) % 2 == 0

for i in range(n):
    t, x, y = map(int, input().split())
    ps.append((t, x, y))

for i in range(1, len(ps)):
    if not f(ps[i][1], ps[i][2], ps[i - 1][1], ps[i - 1][2], ps[i][0] - ps[i - 1][0]):
        print('No')
        break
else:
    print('Yes')