n, k = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(k):
        ans += (i + 1) * 100 + (j + 1)

print(ans)