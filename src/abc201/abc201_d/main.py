h, w = list(map(int, input().split()))
m = []
for i in range(h):
    m.append(input())

def f(x, y, t):
    if t == 0:
        return (0, 0)
    if x < 0 or y < 0:
        return (-1, -1)
    else:
        return (
            max(f(w - 1, h, t - 1)[0], f(w, h - 1, t - 1)[0]),
            max(f(w - 1, h, t - 1)[1], f(w, h - 1, t - 1)[1])
        )

print(f(w, h, w + h))