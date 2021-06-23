n = int(input())

def solve(n):
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                return True
    return False

print('Yes' if solve(n) else 'No')