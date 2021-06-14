import bisect


def solve(a, cs, k):
    i = bisect.bisect_left(cs, k)
    if i == 0:
        return k
    else:
        return a[i - 1] + (k - cs[i - 1])


n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

cs = [a[0] - 1]
for i in range(1, len(a)):
    cs.append(cs[i - 1] + a[i] - a[i - 1] - 1)

for i in range(q):
    k = int(input())
    print(solve(a, cs, k))