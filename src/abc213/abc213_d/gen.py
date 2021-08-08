with open('test/max.in', 'w') as f:
    n = 2 * 10 ** 4
    print(n, file=f)
    for i in range(1, n):
        print(i, i + 1, file=f)