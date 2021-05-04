n, k = map(int, input().split())

def f(x):
    g1, g2 = int(''.join(sorted(str(x))[::-1])), int(''.join(sorted(str(x))))
    return g1 - g2

a = n
for i in range(k):
    a = f(a)

print(a)