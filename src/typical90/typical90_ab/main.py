n = int(input())
grid = [[0 for x in range(1002)] for y in range(1002)]
for i in range(n):
    sx, sy, gx, gy = map(int, input().split())
    gx, gy = gx - 1, gy - 1
    grid[sy][sx] += 1
    grid[gy + 1][gx + 1] += 1
    grid[gy + 1][sx] += -1
    grid[sy][gx + 1] += -1

for y in range(1002):
    for x in range(1, 1002):
        grid[y][x] += grid[y][x - 1]

for y in range(1, 1002):
    for x in range(1002):
        grid[y][x] += grid[y - 1][x]

ans = [0 for _ in range(n + 1)]
for x in range(1002):
    for y in range(1002):
        ans[grid[y][x]] += 1

for a in ans[1:]:
    print(a)