n = int(input())
a = list(map(int, input().split()))
a.sort()
b = list(range(1, n + 1))
print('Yes' if all([a[i] == b[i] for i in range(n)]) else 'No')