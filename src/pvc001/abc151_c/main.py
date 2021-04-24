n, m = map(int, input().split())
cor, pena = 0, 0
hist = [0] * n
for i in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == "AC":
        if hist[p] != -1:
            pena += hist[p]
            cor += 1
            hist[p] = -1
    else:
        if hist[p] != -1:
            hist[p] += 1

print(cor, pena)