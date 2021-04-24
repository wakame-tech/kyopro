import numpy as np
bingo = []
for i in range(3):
    bingo.append(list(map(int, input().split())))

bingo = np.array(bingo)
flags = np.zeros_like(bingo, dtype=bool)

n = int(input())
for i in range(n):
    b = int(input())
    for x, y in np.ndindex(bingo.shape):
        if bingo[x, y] == b:
            flags[x, y] = True

def is_bingo(bingo):
    conds = []
    conds.append(np.diag(flags))
    conds.append(np.diag(np.fliplr(flags)))
    for i in range(3):
        conds.append(bingo[i, :])
        conds.append(bingo[:, i])

    print(cond)
    return any(map(lambda cond: np.all(cond), conds))

print('Yes' if is_bingo(bingo) else 'No')