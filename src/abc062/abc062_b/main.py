h, w = list(map(int, input().split()))
a = [input() for _ in range(h)]
aa = [['#' for x in range(w + 2)] for y in range(h + 2)]
for i in range(h):
    for j in range(w):
        aa[i + 1][j + 1] = a[i][j]

for i in range(h + 2):
    for j in range(w + 2):
        print(aa[i][j], end='')
    print()