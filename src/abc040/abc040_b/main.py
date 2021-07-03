n = int(input())

ans = 10 ** 9
for i in range(1, 1000):
    for j in range(1, 1000):
        if n < i * j:
            break
        ans = min(ans, n - i * j + abs(i - j))

print(ans)
