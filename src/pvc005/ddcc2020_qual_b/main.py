n = int(input())
a = list(map(int, input().split()))

d = [0]
for e in a:
    d.append(d[-1] + e)

s = d[-1]
ans = 10 ** 10
for e in d:
    ans = min(ans, abs(e - (s - e)))

print(ans)