n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))

def cost(f, t, a):
    cost = 0
    for pos in range(f, t, -1 if f > t else 1):
        if pos in a:
            cost += 1
    return cost

print(min(cost(x, 0, a), cost(x, n, a)))