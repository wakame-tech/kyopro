a, b, x = list(map(int, input().split()))

ans = 0
for i in range(1, 11):
    n, lim = (x - b * i) // a, 10 ** 9 if i == 10 else 10 ** i - 1
    ans = max(ans, min(n, lim))

print(ans)