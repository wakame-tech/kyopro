n = int(input())
a = list(map(int, input().split()))

h = {}
ans = 0
for i, e in enumerate(a):
    if (i + 1, e) in h:
        ans += 1
    else:
        h[(e, i + 1)] = True

print(ans)