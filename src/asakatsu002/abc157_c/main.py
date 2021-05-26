n, m = list(map(int, input().split()))

def ok(k, n, conds):
    ks = str(k)
    if len(ks) != n:
        return False
    for s, c in conds:
        if len(ks) < s + 1:
            return False
        if int(ks[s]) != c:
            return False
    return True

def solve(n, m):
    conds = []
    for _ in range(m):
        s, c = list(map(int, input().split()))
        conds.append((s - 1, c))

    for i in range(1001):
        if ok(i, n, conds):
            return i
    return -1

print(solve(n, m))