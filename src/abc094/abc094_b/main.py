n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))

def cost(f, t, a):
    c = 0
    for i in range(f, t, -1 if f > t else 1):
        if i + 1 in a:
            c += 1
    return c

print(min(cost(x, 0, a), cost(x, n - 1, a)))