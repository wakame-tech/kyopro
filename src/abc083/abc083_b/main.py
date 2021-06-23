n, a, b = list(map(int, input().split()))

ans = 0
for i in range(n + 1):
    s = sum(map(int, list(str(i))))
    if a <= s <= b:
        ans += i

print(ans)