from itertools import product

n = int(input())
ranges = []
for i in range(n):
    l, r = map(int, input().split())
    ranges.append((l, r))

# n = 3
# ranges = [(1, 3), (2, 4), (1, 2)]

ans = 0.0
for (i, j) in product(range(n), repeat=2):
    if i >= j:
        continue
    # print(f'{i=} {j=}')
    pats = 0
    li, ri = ranges[i]
    lj, rj = ranges[j]
    al = (ri + 1 - li) * (rj + 1 - lj)
    # 転倒したい -> 自分の方がより大きい
    for k in range(li, ri + 1):
        # k より小さい [L_j, R_j] の個数 = [L_j, min(k - 1, R_j)]
        p = max(0, min(k - 1, rj) - lj + 1)
        # print(f'{k=}: [{lj}..{min(k - 1, rj)}] = {p}')
        pats += p

    # print(f'{pats=} / {al=}')
    ans += pats / al

print(ans)