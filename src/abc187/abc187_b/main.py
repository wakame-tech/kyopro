n = int(input())
ps = []
for i in range(n):
  x, y = map(int, input().split(' '))
  ps.append((x, y))

c = 0
for j in range(n):
  for i in range(j):
    dx, dy = ps[j][0] - ps[i][0], ps[j][1] - ps[i][1]
    if dx == 0:
      continue
    l = dy / dx
    if -1 <= l and l <= 1:
      c += 1

print(c)