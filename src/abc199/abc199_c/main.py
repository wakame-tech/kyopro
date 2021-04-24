n, s, q = int(input()), list(input()), int(input())

def swap(f, l, i, j, n):
    si, sj = f[i] if i < n else l[i - n], f[j] if j < n else l[j - n]
    if j < n:
        f[j] = si
    else:
        l[j - n] = si
    if i < n:
        f[i] = sj
    else:
        l[i - n] = sj

    return f, l
    
f, l = s[:n], s[n:]
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        f, l = swap(f, l, a - 1, b - 1, n)
    if t == 2:
        f, l = l, f

print(''.join([*f, *l]))