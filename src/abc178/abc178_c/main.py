n = int(input())

if n == 1:
    print(0)
else:
    m = 10 ** 9 + 7
    ans = pow(10, n, m) - (2 * pow(9, n, m) - pow(8, n, m))
    ans %= m
    print(ans)
