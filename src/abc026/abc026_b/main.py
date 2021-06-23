import math

n = int(input())
rs = [int(input()) for i in range(n)]
rs = rs[::-1]
rs.append(0)
rs.sort(reverse=True)
ans = 0
for i, r in enumerate(rs):
    ans += (1 if i % 2 == 0 else -1) * (rs[i] ** 2)

ans *= math.pi

print(ans)