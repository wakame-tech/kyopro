s = input()

def solve(s):
    for i in range(len(s)-1, -1, -1):
        if i % 2 == 1:
            continue
        if s[:i // 2] == s[i // 2:i]:
            return i

print(solve(s))