n = int(input())

def solve(n):
    for i in range(100):
        for j in range(100):
            if i * 4 + 7 * j == n:
                return True
    return False

print('Yes' if solve(n) else 'No')