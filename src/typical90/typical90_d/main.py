h, w = list(map(int, input().split()))
a = []
h_sum = [0 for _ in range(h)]
v_sum = [0 for _ in range(w)]
for i in range(h):
    aa = list(map(int, input().split()))
    a.append(aa)
    h_sum[i] = sum(aa)
    for j in range(w):
        v_sum[j] += aa[j]

for i in range(h):
    for j in range(w):
        print(h_sum[i] + v_sum[j] - a[i][j], end=' ')