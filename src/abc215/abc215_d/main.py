n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

def prime_factorize(n: int) -> set:
    """
    素因数分解
    """
    a = set()
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a

flags = [True for _ in range(10 ** 5 + 1)]
for i in range(n):
    d = prime_factorize(a[i])
    for j in d:
        if flags[j]:
            for k in range(j, m + 1, j):
                flags[k] = False

ans = []
for i in range(1, m + 1):
    if flags[i]:
        ans.append(i)

print(len(ans))
print(*ans, sep='\n')