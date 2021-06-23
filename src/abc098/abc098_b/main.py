n = int(input())
s = input()

ans = 0
for i in range(1, n - 1):
    p, q = set(list(s[:i])), set(list(s[i:]))
    ans = max(ans, len(p.intersection(q)))

print(ans)