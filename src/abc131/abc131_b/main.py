n, l = list(map(int, input().split()))
s = sum(l + i for i in range(n))

df = 10 * 9
ans = 0
for i in range(n):
    d = abs(l + i)
    if d < df:
        ans = s - (l + i)
        df = d

print(ans)