with open('test/max.in', 'w') as f:
    n = 10 ** 3
    m = n - 1
    print(n, m, file=f)
    for i in range(m):
        print(i + 1, i + 2, file=f)

with open('test/max.out', 'w') as f:
    print(0, file=f)