n = int(input())
s = sum(int(c) for c in str(n))
print('Yes' if n % s == 0 else 'No')