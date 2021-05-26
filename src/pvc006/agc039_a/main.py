s, k = list(input()), int(input())

ans = 0
for p in range(1, len(s)):
    if s[p] == s[p - 1]:
        ans += 1


if k >= 2:
    ans2 = 0
    ss = s + s
    for p in range(1, len(ss)):
        if ss[p] == ss[p - 1]:
            ans2 += 1

    print(ans * k + (ans2 - ans * 2) * k - 1)

print(ans)