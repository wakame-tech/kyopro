n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = n * m - sum(a)
print(-1 if b >= k else max(0, b))