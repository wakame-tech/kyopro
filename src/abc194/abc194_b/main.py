n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

ans = 10 ** 5
for i in range(n):
    for j in range(n):
        if i == j:
            ans = min(ans, data[i][0] + data[i][1])
        else:
            ans = min(ans, max(data[i][0], data[j][1]))

print(ans)
