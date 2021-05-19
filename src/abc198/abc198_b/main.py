n = int(input())

def solve(s: str):
    for i in range(19):
        t = s.zfill(i + len(s))
        l = len(t) // 2 + 1
        if t[:l] == t[::-1][:l]:
            return True
    return False

print('YNeos'[not solve(str(n))::2])