n = int(input())
hist = set()
cnt = 0
a, b = 2, 2
while True:
    b = 2
    if a ** b > n:
        break
    while True:
        if a ** b > n:
            break

        if not a ** b in hist:
            hist.add(a ** b)
            cnt += 1
        b += 1
    a += 1
print(n - cnt)
