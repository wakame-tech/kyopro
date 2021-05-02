from collections import deque

s = input()
t = deque()
f = False
for c in s:
    if c == 'R':
        f = not f
    else:
        if f:
            if len(t) != 0 and c == t[0]:
                t.popleft()
            else:
                # t = c + t
                t.appendleft(c)
        else:
            if len(t) != 0 and t[-1] == c:
                t.pop()
            else:
                # t = t + c
                t.append(c)

t = list(t)
if f:
    t = t[::-1]

print(''.join(t))