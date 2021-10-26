from itertools import combinations

n = int(input())
a = []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append((x, y))

ans = 0
for p1, p2, p3 in combinations(a, 3):
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p1[0]
    y2 = p3[1] - p1[1]
    # ans += 1
    if x1 * y2 != x2 * y1:
        ans += 1

print(ans)