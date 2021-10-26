h, w = list(map(int, input().split()))
a = []
for i in range(h):
    b = list(map(int, input().split()))
    a.append(b)


def ok():
    for i1 in range(h):
        for i2 in range(h):
            if i1 >= i2:
                continue
            for j1 in range(w):
                for j2 in range(w):
                    if j1 >= j2:
                        continue

                    if not (a[i1][j1] + a[i2][j2] <= a[i2][j1] + a[i1][j2]):
                        return False

    return True


print("Yes" if ok() else "No")
