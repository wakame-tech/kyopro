from collections import deque

n = int(input())
a = list(map(int, input().split()))
a = deque(a)
md = 998244353
dp = [[0 for x in range(10)] for y in range(n - 1)]

x = deque.popleft(a)
y = deque.popleft(a)
dp[0][(x + y) % 10] += 1
dp[0][(x * y) % 10] += 1

# print(dp[0])

for i in range(n - 2):
    y = deque.popleft(a)
    for x in range(10):
        dp[i + 1][(x + y) % 10] += dp[i][x] % md
        dp[i + 1][(x * y) % 10] += dp[i][x] % md
        # print(f'({x=} {y=} {x + y % 10} {x * y % 10})')

# print(dp)

for i in range(10):
    print(dp[n - 2][i] % md)