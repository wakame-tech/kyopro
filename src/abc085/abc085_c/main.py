n, y = map(int, input().split())

def solve():
    for i in range(2001):
        for j in range(2001):
            if i * 10000 + j * 5000 + (n - i - j) * 1000 == y and n - i - j >= 0:
                return i, j, n - i - j
    return -1, -1, -1

print(' '.join(map(str, solve())))