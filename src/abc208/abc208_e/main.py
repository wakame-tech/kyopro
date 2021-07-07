import math

n, K = list(map(int, input().split()))
digits = math.ceil(math.log10(n))

# [桁の積, 組み合わせ]
dp = [[0 for x in range(10)] for y in range(digits)]
for i in range(10):
    if i <= n:
        dp[0][i] = 1

def dbg(digits, dp):
    for i in range(digits):
        print(f'{10 ** i}:', end=' ')
        for j in range(10):
            print(dp[i][j], end=' ')
        print()

# dbg(digits, dp)

for i in range(1, digits):
    for j in range(10):
        if n < 10 ** i + j:
            continue
        cnt = 0
        for k in range(10):
            prd = dp[i - 1][k] * j
            # print(f'{dp[i - 1][k]}, {j}, {prd=} {K}, {n} >? {10 ** i * k + j}')
            if prd <= K and n >= 10 ** k + j:
                cnt += 1
        dp[i][j] = cnt
        # print(f'dp[{i=}][{j=}] = {dp[i][j]}')

# dbg(digits, dp)

print(sum(dp[-1]))