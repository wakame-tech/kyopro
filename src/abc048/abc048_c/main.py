n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [0, *a]

ans = 0
for i in range(n):
    if a[i] + a[i + 1] > x:
        ans += a[i] + a[i + 1] - x
        a[i + 1] -= a[i] + a[i + 1] - x

print(ans)