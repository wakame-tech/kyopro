h, w = list(map(int, input().split()))
g = []
for i in range(h):
    g.append(input())

for i in range(h):
    for j in range(w):
        if all(g[k][j] == '.' for k in range(h)) or all(g[i][k] == '.' for k in range(w)):
            continue
        print(g[i][j], end='')
    print()