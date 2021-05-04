h, w, y, x = map(int, input().split())
m = []
ds = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(h):
    m.append(input())

ans = 0
for d in ds:
    s = (x + d[0] - 1, y + d[1] - 1)
    while 0 <= s[0] < w and 0 <= s[1] < h and m[s[1]][s[0]] == ".":
        ans += 1
        s = (s[0] + d[0], s[1] + d[1])

print(ans + 1)