n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
pre = a[0] - 1
for i in range(n):
    ans += b[a[i] - 1]
    if pre + 1 == a[i] - 1:
        ans += c[pre]
    pre = a[i] - 1
print(ans)