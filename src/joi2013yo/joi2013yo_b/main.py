n = int(input())
d = []
for i in range(n):
    s1, s2, s3 = list(map(int, input().split()))
    d.append([s1, s2, s3])

ans = [0 for _ in range(n)]
for i in range(3):
    for j in range(n):
        if [d[k][i] for k in range(n)].count(d[j][i]) == 1:
            ans[j] += d[j][i]

for i in range(n):
    print(ans[i])