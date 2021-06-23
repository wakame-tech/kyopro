n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if len(set([l[i], l[j], l[k]])) == 3 and l[i] + l[j] > l[k] and abs(l[i] - l[j]) < l[k]:
                ans += 1

print(ans)