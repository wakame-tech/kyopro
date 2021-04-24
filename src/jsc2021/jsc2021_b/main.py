n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(10 ** 3 + 1):
    if (i in a) ^ (i in b):
        print(i, end=' ')