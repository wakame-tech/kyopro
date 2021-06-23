x, y = list(map(int, input().split()))

def solve(x, y):
    for i in range(100):
        for j in range(100):
            if i + j == x and i * 4 + j * 2 == y:
                return True
    return False

print('Yes' if solve(x, y) else 'No')