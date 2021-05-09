from math import factorial

def ncr(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)

n = int(input())
a = list(map(int, input().split()))

h = {}
for e in a:
    k = str(e % 200).zfill(2)
    if k not in h:
        h[k] = [e]
    else:
        h[k].append(e)

ans = 0
for k, v in dict.items(h):
    l = len(v)
    if l >= 2:
        ans += ncr(l, 2)

print(ans)
