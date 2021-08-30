def eratosthenes(n: int):
    """
    素因数種類数
    """
    c = [0] * (n + 1)
    for i in range(2, n + 1):
        if c[i] == 0:
            for j in range(i, n + 1, i):
                c[j] += 1
    return c


n, k = list(map(int, input().split()))
res = eratosthenes(n)
ans = 0
for e in res:
    if e >= k:
        ans += 1

print(ans)