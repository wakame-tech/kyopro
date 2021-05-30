import bisect

n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if abs(i - j) < k < i + j:
                ans += 1
        # k_l, k_r = bisect.bisect_left(l, abs(l[i] - l[j]) + 1), bisect.bisect_right(l, l[i] + l[j] - 1)
        # # print(f'(i, j) = ({i}, {j}), {k_l}..{k_r}')
        # for k in range(k_l + 1, k_r):
        #     if i != j and j != k and k != i:
        #         # print(i, j, k)
        #         ans += 1

print(ans)