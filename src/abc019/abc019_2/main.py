s = input()
b = s[0]
ans = ''
for i in range(1, len(s)):
    if b[-1] != s[i]:
        ans += f'{b[-1]}{len(b)}'
        b = s[i]
    else:
        b += s[i]
ans += f'{b[-1]}{len(b)}'

print(ans)