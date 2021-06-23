n, k = list(map(int, input().split()))
m = [0 for i in range(n)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        m[a[j] - 1] += 1
ans = sum(map(lambda e: e == 0, m))
print(ans)