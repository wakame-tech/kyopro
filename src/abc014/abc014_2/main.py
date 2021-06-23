n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
bits = list(map(int, list(str(bin(x))[2:].ljust(n, '0'))))
print(sum([a[i] * bits[i] for i in range(n)]))