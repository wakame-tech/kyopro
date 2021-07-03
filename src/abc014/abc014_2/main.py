n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

if x == 0:
    print(0)
    exit()

ans = 0
i = 0
while x != 0:
    if x % 2 == 1:
        ans += a[i]
    i += 1
    x //= 2

print(ans)