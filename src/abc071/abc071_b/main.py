import bisect

s = input().strip()
cs = [0 for i in range(26)]
for c in s:
    cs[ord(c) - ord('a')] = 1

try:
    i = cs.index(0)
except:
    i = -1
if i == -1:
    print('None')
else:
    print(chr(ord('a') + i))