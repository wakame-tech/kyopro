n = int(input())
a = list(map(int, input().split()))
ca = [0]
for i in range(0, n):
    ca.append(ca[i] + a[i])

for k in range(1, n + 1):
    print(max([ca[i] - ca[i - k] for i in range(k, n + 1)]))