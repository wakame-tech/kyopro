n, m = list(map(int, input().split()))
d = {}
for i in range(m):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    if a > b:
        a, b = b, a
    d[(a, b)] = 1

def has(d, i, j):
    if i > j:
        return (j, i) in d
    else:
        return (i, j) in d

def ok(d, n):
    for i in range(n):
        if has(d, i, 0) and has(d, i, n - 1):
            return True
    return False

print('POSSIBLE' if ok(d, n) else 'IMPOSSIBLE')