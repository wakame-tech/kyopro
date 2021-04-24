n = int(input())
ts = list(map(int, input().split()))
s = sum(ts)
m = int(input())
ps = []
for i in range(m):
    p, x = map(int, input().split())
    ps.append((p, x))

for i in range(m):
    print(s - ts[ps[i][0] - 1] + ps[i][1])