n = int(input())
s = sum(map(int, str(n)))
print('Yes' if n % s == 0 else 'No')