n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m, M = 0, 1000
for i in range(n):
    m = max(m, a[i])
    M = min(M, b[i])

print(max(0, M - m + 1))