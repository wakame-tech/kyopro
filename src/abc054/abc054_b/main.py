n, m = list(map(int, input().split()))
a = [input() for i in range(n)]
b = [input() for i in range(m)]

def match(a, x, y, b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if a[y + i][x + j] != b[i][j]:
                return False
    return True

def solve(a, b):
    for i in range(len(a) - len(b)):
        for j in range(len(a[0]) - len(b[0])):
            if not match(a, j, i, b):
                return False

    return True

print('Yes' if solve(a, b) else 'No')