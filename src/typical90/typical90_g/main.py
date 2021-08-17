import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for i in range(q)]

a.sort()

for e in b:
    i = bisect.bisect_left(a, e)
    if i == 0:
        print(abs(a[i] - e))
    elif i == n:
        print(abs(a[i - 1] - e))
    else:
        print(min(abs(a[i] - e), abs(a[i - 1] - e)))