a, b, c = list(map(int, input().split()))
m = a % b

def solve(m, b, c):
    if m == 0:
        return False
    for i in range(100):
        if (m * i) % b == c:
            return True
    return False

print('YES' if solve(a % b, b, c) else 'NO')