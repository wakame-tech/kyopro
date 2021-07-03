n, l = list(map(int, input().split()))

def aji(n, l, j):
    return sum(l + i for i in range(n) if i != j)

ans, min_abs = 0, 10 ** 9
for i in range(n):
    a = abs(aji(n, l, -1) - aji(n, l, i))
    if a < min_abs:
        ans = aji(n, l, i)
        min_abs = a

print(ans)