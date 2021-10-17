s = input()

a = []
for i in range(len(s)):
  a.append(s[i:] + s[:i])

a.sort()

print(a[0])
print(a[-1])