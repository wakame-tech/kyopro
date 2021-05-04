s = input()
l = ['dream', 'dreamer', 'erase', 'eraser']

def solve(s):
    i = len(s)
    while i > 0:
        for e in l:
            if s[i - len(e):i] == e:
                i -= len(e)
                break
        else:
            return False
    return True

print('YES' if solve(s) else 'NO')