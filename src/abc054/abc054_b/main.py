import numpy as np

n, m = list(map(int, input().split()))
a = np.array([list(input()) for i in range(n)])
b = np.array([list(input()) for i in range(m)])

def solve(n, m, a: np.ndarray, b: np.ndarray):
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if np.array_equal(a[i:i+m, j:j+m], b):
                return True

    return False

print('Yes' if solve(n, m, a, b) else 'No')