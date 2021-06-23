s = input()

ans = 0
for i in range(len(s)):
    cnt = 0
    for c in s[i:]:
        if c in 'ACGT':
            cnt += 1
        else:
            break
    ans = max(ans, cnt)

print(ans)