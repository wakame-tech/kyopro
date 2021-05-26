n, k = list(map(int, input().split()))
ts = [int(input()) for _ in range(n)]

for i in range(3, n):
    if sum(ts[i-3:i]) < k:
        print(i)
        break
else:
    print(-1)