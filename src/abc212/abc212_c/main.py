n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

al = []
for i in range(n):
    al.append((a[i], True))
for i in range(m):
    al.append((b[i], False))

al.sort(key=lambda x: x[0])


ans = 10 ** 9
pre_a, pre_b = a[0], b[0]
for i in range(n + m):
    if al[i][1]:
        pre = pre_b
    else:
        pre = pre_a

    ans = min(ans, abs(al[i][0] - pre))

    if al[i][1]:
        pre_a = al[i][0]
    else:
        pre_b = al[i][0]

print(ans)