s, t = input(), input()

def rot(s, i):
    return s[i:] + s[:i]

def solve(s, t):
    for i in range(len(s)):
        if rot(s, i) == t:
            return True
    return False

print('Yes' if solve(s, t) else 'No')