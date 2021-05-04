n, m, t = map(int, input().split())
arr = []
for i in range(m):
    a, b = map(int, input().split())
    arr.append((a, b))

r = n
c = 0
for a, b in arr:
    r -= a - c
    if r <= 0:
        break
    c = a
    r += min(n - r, b - a)
    c = b
    
r -= t - arr[-1][1]

print("Yes" if r > 0 else "No")
