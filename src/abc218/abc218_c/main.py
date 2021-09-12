import numpy as np

# n=int(input())
# s, t = [], []
# for i in range(n):
#     ss = input()
#     r = []
#     for j in range(n):
#         if ss[j] == ".":
#             r.append(False)
#         else:
#             r.append(True)
#     s.append(r)

# for i in range(n):
#     ss = input()
#     r = []
#     for j in range(n):
#         if ss[j] == ".":
#             r.append(False)
#         else:
#             r.append(True)
#     t.append(r)

n = 200
s = np.zeros((200, 200), dtype=bool)
t = np.ones((200, 200), dtype=bool)
s, t = np.array(s), np.array(t)

# 200 * 200 * 4 * 200 * 200
for dx in range(n + 1):
    for dy in range(n + 1):
        for rot in range(4):
            ss = np.rot90(np.roll(s, (dx, dy)), rot)
            if (ss == t).all():
                print('Yes')
                exit()

print('No')