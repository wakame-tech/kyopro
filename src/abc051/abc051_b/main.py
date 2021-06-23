k,s = list(map(int, input().split()))
k = k + 1
ans = 0
for i in range(k):
    for j in range(k):
        for l in range(k):
            if i + j + l == s:
                ans += 1

print(ans)