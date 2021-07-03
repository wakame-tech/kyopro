n = int(input())
d = {}
ans = 0
for i in range(n):
    a = int(input())
    if a - 1 in d:
        ans += 1
    d[a - 1] = True

print(ans)