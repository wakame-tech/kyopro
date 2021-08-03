import numpy as np

n, m, k = list(map(int, input().split()))
g = [[1 for x in range(n)] for y in range(n)]

for i in range(m):
    u, v = list(map(int, input().split()))
    g[u - 1][v - 1] = 0
    g[v - 1][u - 1] = 0

for i in range(n):
    g[i][i] = 0

def mat_mul(a, b, m) :
    a, b = np.array(a, dtype=np.longlong), np.array(b, dtype=np.longlong)
    return (a @ b % m).tolist()
    # I, J, K = len(a), len(b[0]), len(b)
    # c = [[0] * J for _ in range(I)]
    # for i in range(I) :
    #     for j in range(J) :
    #         for k in range(K) :
    #             c[i][j] += a[i][k] * b[k][j]
    #         c[i][j] %= m
    # return c


def mat_pow(x, n, m):
    y = [[0] * len(x) for _ in range(len(x))]

    for i in range(len(x)):
        y[i][i] = 1

    while n > 0:
        if n & 1:
            y = mat_mul(x, y, m)
        x = mat_mul(x, x, m)
        n >>= 1
    return y

# print(g)
ans = mat_pow(g, k, 998244353)
# print(ans)
print(ans[0][0])