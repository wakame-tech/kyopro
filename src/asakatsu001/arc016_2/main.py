n = int(input())
m = []
for i in range(n):
    m.append(input())

pressing = set()
cnt = 0

for h in range(n - 1, -1, -1):
    for w in range(9):
        if m[h][w] == 'x':
            cnt += 1
        if m[h][w] == 'o' and w not in pressing:
            cnt += 1
            pressing.add(w)
        if m[h][w] != 'o' and w in pressing:
            pressing.remove(w)

print(cnt)