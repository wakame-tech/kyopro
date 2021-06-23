a, b, c, k = list(map(int, input().split()))
m = k - (a + b)
print(a if m <= 0 else a - m)