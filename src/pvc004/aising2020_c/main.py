n = int(input())
m = 10 ** 4

def f(i, j, k):
    return i ** 2 + j ** 2 + k ** 2 + i * j + j * k + k * i

ans = [0] * (m + 1)
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            v = f(i, j, k)
            if v <= m:
                ans[v] += 1

for i in range(1, n + 1):
    print(ans[i])