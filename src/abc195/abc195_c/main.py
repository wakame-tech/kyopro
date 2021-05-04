n = int(input())
# 1 ~ 999 -> 0 * (999 - 1 + 1) = 0
# 1,000 ~ 999,999 -> 1 * (999999 - 1000 + 1) = (10 ** 6 - 10 ** 3)
# 1,000,000 - 999,999,999 -> 2 * (10 ** 9 - 10 ** 6)

# l = int(log10(n))
# n -> (k // 3) * (n - 10 ^ (k // 3) * 3) + 1)
l = len(str(n))

ans = 0
for k in range(0, l, 3):
    e = min(n, 10 ** (k + 3) - 1)
    # print(f'{k // 3} commas: 10^{k} ~ {e} => {e - (10 ** k) + 1}')
    ans += k // 3 * (e - (10 ** k) + 1)

print(ans)