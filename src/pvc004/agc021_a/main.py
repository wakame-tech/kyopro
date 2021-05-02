n = [int(i) for i in input()]
if len(n) == 1:
    print(n[0])
    exit()
k = len(n) - 1
a = ((n[0] - 1) * 10 ** k) + (10 ** k) - 1
a = sum([int(c) for c in str(a)])
b = int(''.join(map(str, n))) - (n[-1] + 1)
b = sum([int(c) for c in str(b)])
c = sum([int(c) for c in n])
print(max(a, b, c))