h, w = map(int, input().split())
m = []
for i in range(h):
    m.append(input())

def sharps(reg):
    return len(list(filter(lambda c: c == '#', reg)))

corners = 0
for i in range(h - 1):
    for j in range(w - 1):
        r = [m[i][j], m[i][j + 1], m[i + 1][j], m[i + 1][j + 1]]
        if (c := sharps(r)) == 1 or c == 3:
            corners += 1

print(corners)