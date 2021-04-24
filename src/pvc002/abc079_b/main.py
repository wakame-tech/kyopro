n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    n1, n2, n3 = 2, 1, 3
    for i in range(n - 2 + 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(n3)