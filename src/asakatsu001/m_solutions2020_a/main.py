x = int(input())

def f(x):
    cs = [(200 * i, k) for i, k in zip(range(2, 11), range(8, 0, -1))]
    for c, k in cs:
        if c <= x < c + 200:
            return k

print(f(x))