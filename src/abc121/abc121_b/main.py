n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    if sum(ai * bi for ai, bi in zip(a, b)) + c > 0:
        ans += 1

print(ans)