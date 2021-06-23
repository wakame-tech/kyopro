a, b, c, d = list(map(int, input().split()))
print(len(set(range(a, b)).intersection(set(range(c, d)))))