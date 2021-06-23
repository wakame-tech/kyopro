n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

ans = 0
for i in range(n):
    ans = max(0, ans, s.count(s[i]) - t.count(s[i]))

print(ans)