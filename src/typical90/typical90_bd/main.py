n, s = list(map(int, input().split()))
w = []
for i in range(n):
    a, b = list(map(int, input().split()))
    w.append((a, b))

# n, s = 3, 15
# w = [(4, 2), (7, 3), (5, 8)]


def dgb(dp):
    for i in range(n + 1):
        for j in range(s):
            print("o" if dp[i][j] else ".", end=" ")
        print()
    print()


dp = [[False for x in range(s + 1)] for y in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(s + 1):
        if dp[i][j]:
            na, nb = j + w[i][0], j + w[i][1]
            if na < s + 1:
                dp[i + 1][na] = True
            if nb < s + 1:
                dp[i + 1][nb] = True

# dgb(dp)

if not dp[n][s]:
    print("Impossible")
    exit()

ans = []
j = s
for i in reversed(range(1, n + 1)):
    a, b = w[i - 1]
    if j - a >= 0 and dp[i - 1][j - a]:
        j -= a
        ans.append("A")
    elif j - b >= 0 and dp[i - 1][j - b]:
        j -= b
        ans.append("B")

print("".join(reversed(ans)))
