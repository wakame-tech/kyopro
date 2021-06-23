n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = n - sum(a)
print(-1 if ans < 0 else ans)