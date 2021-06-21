n = int(input())
print(sum(n / (n - i) for i in range(1, n)))