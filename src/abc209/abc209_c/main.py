n = int(input())
c = list(map(int, input().split()))
c.sort()
ans = c[0]
for i in range(1, n):
    ans *= max(0, c[i] - i)
    ans %= 10 ** 9 + 7
print(ans % (10 ** 9 + 7))