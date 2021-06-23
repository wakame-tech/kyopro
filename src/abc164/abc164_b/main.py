a, b, c, d = list(map(int, input().split()))

def f(a, b, c, d):
    while True:
        c -= b
        if c <= 0:
            return True
        a -= d
        if a <= 0:
            return False

print('Yes' if f(a, b, c, d) else 'No')