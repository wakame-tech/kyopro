n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    ans += min(b[i - 1], a[i - 1] + a[i])

print(ans)