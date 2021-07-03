n = int(input())
s = input()

def solve(s):
    t = 'b'
    i = 0
    if s == t:
        return 0

    while len(t) <= len(s):
        if i % 3 == 0:
            t = 'a' + t + 'c'
        elif i % 3 == 1:
            t = 'c' + t + 'a'
        else:
            t = 'b' + t + 'b'
        if s == t:
            return i + 1
        i += 1
    return -1

print(solve(s))