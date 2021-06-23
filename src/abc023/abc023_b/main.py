n = int(input())
s = input()

def solve(s):
    i = len(s) // 2
    d = 1
    if s[i] != 'b':
        return -1

    while True:
        if i - d == 0:
            return i
        if s[i - d] == 'acb'[(d - 1) % 3] and s[i + d] == 'cab'[(d - 1) % 3]:
            d += 1
        else:
            return -1

print(solve(s))