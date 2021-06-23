n = int(input())
s = input()

v = 0
mx = 0
for i in range(n):
    if s[i] == 'I':
        v += 1
    else:
        v -= 1
    mx = max(mx, v)

print(mx)