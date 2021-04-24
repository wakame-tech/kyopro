n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    mn = a[i]
    for j in range(i, n):
        if a[j] < mn:
            mn = a[j]
        ans = max(ans, (j - i + 1) * mn)

print(ans)