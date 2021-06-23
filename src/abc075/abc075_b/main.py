h, w = list(map(int, input().split()))
ss = [list(input()) for _ in range(h)]
s = [['.' for x in range(w + 2)] for y in range(h + 2)]

for i in range(h):
    for j in range(w):
        s[i + 1][j + 1] = ss[i][j]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '#':
            continue
        cnt = 0

        for k in range(3):
            for l in range(3):
                if s[i + k - 1][j + l - 1] == '#':
                    cnt += 1
        s[i][j] = str(cnt)

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(s[i][j], end='')
    print()
