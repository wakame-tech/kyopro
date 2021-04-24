n = int(input())
xs = []
for i in range(n):
  xs.append(list(map(int, input().split(' '))))

xs = list(sorted(xs, key=lambda e: 2 * e[0] + e[1], reverse=True))
ao, tk = sum(map(lambda e: e[0], xs)), 0
c = 0
for x in xs:
  if ao < tk:
    break

  ao -= x[0]
  tk += x[0] + x[1]
  c += 1

print(c)