import math

def cnt(c, k):
    return math.ceil((c - 1) / (k - 1))

n, k = map(int, input().split())
a = list(map(int, input().split()))
# i = a.index(1)

# if n == k:
#     print(1)
# else:
#     l, r = i + 1, n - i
#     lc, rc = cnt(l, k), cnt(r, k)
#     # print(f'{l}: {lc}, {r}: {rc}')
#     print(lc + rc)

print(cnt(n, k))