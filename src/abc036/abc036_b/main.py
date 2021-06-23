n = int(input())
s = [input() for i in range(n)]

for i in range(n):
    for j in range(n):
        print(s[n - 1 - j][i], end='')

    print()

