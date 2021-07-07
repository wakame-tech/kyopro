n = int(input())
a = list(map(int, input().split()))

ans = [1]
for i in range(1, n):
    if a[i - 1] < a[i]:
        ans.append(ans[i - 1] + 1)
    else:
        ans.append(1)

print(sum(ans))