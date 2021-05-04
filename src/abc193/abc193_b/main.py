n = int(input())

ans = 10 ** 9
for i in range(n):
    a, p, x = map(int, input().split())
    if x - a > 0:
        ans = min(ans, p)

print(-1 if ans == 10 ** 9 else ans)