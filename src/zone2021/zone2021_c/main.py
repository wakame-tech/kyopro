import numpy as np

def rank(l):
    n = len(l) - 1
    li = [(i, v) for (i, v) in enumerate(l)]
    return [e[0] for e in sorted(li, key=lambda e: e[1])]

print(rank([3, 7, 1]))

exit()

n = int(input())
l = []
for i in range(n):
    a, b, c, d, e = map(int, input().split())
    l.append([a, b, c, d, e])

l = np.array(l)

# dp = [[[0 for k in range(3)] for j in range(n)] for i in range(5)]
dp = np.array([[10 ** 9 for j in range(5)] for i in range(n)])
for i in range(n):
    dp[i, 0] = l[i, 0]

for i in range(1, 5):
    # pre = list(sorted(l[:, i], reverse=True))[:3]
    # print(f'top 3: {pre}')
    for j in range(n):
        dp[j, i] = min(dp[j, i], dp[j, i - 1] + l[j, i])
        # dp[i][j] = pre
        # for k in range(3):
        #     dp[i][j][k] = min(dp[i][j][k] + l[i, j], pre[k])

print(dp)