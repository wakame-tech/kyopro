w, a, b = list(map(int, input().split()))
if a > b + w:
    print(max(0, a - (b + w)))
else:
    print(max(0, b - (a + w)))