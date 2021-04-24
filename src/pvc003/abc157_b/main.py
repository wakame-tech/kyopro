# bingo = []
# for i in range(3):
#     bingo.append(list(map(int, input().split())))

# n = int(input())
# for i in range(n):
#     b = int(input())
#     for j in range(3):
#         for k in range(3):
#             if bingo[j][k] == b:
#                 bingo[j][k] = -1

# def is_bingo(bingo):
#     for i in range(3):
#         if bingo[i][0] == bingo[i][1] == bingo[i][2] == -1:
#             return True

#     for i in range(3):
#         if bingo[0][i] == bingo[1][i] == bingo[2][i] == -1:
#             return True

#     if bingo[0][0] == bingo[1][1] == bingo[2][2] == -1:
#         return True
    
#     if bingo[0][2] == bingo[1][1] == bingo[2][0] == -1:
#         return True

#     return False

# print('Yes' if is_bingo(bingo) else 'No')

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
        conds.append(flags[i, :])
        conds.append(flags[:, i])

    # print(conds)
    return any(map(lambda cond: np.all(cond), conds))

print('Yes' if is_bingo(bingo) else 'No')