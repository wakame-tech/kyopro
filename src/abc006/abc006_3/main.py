n,m=list(map(int, input().split()))

def solve(n,m):
    for y in range(10 ** 5 + 1):
        zz = m - 2 * n - y
        if zz < 0:
            break
        if zz % 2 == 0:
            z = zz // 2
            if n < (y + z):
                continue
            return n - (y + z), y, z

    return -1, -1, -1

print(*solve(n, m))