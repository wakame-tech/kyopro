import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))

ac = [0]
for i in range(1, n + 1):
    ac.append(ac[i - 1] + a[i - 1])

ans = 0
for s in range(1, n + 1):
    i = bisect.bisect_left(ac, k + ac[s - 1], lo=s)
    # print(f's: {s}, i={i}')
    ans += n - i + 1

print(ans)