n, m = map(int, input().split())
a = [[0 for j in range(n + 2)] for i in range(n)]
for i in range(1, n):
    for j in range(1, i + 2):
        # l. r: 左右からの負荷, m: 追加でかかる重量
        l, r, w = a[i - 1][j - 1], a[i - 1][j], m if j in [1, i + 1] else 2 * m
        a[i][j] += (l + r + w) / 2

for i in range(n):
    for j in range(1, i + 2):
        print(round(a[i][j]), end=' ')
    print('')