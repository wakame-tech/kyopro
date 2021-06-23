n = int(input())
d = [False for _ in range(n)]
ans = 0
for i in range(n):
    a = int(input())
    if d[a - 1]:
        ans += 1
    d[a - 1] = True

print(ans)