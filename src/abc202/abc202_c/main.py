from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
# for i in range(n):
#     for j in range(n):
#         if a[i] == b[c[j] - 1]:
#             ans += 1

bb = [b[c[i] - 1] for i in range(n)]
c1, c2 = Counter(a), Counter(bb)
com = set(a).intersection(set(bb))
for k in com:
    ans += c1[k] * c2[k]

print(ans)