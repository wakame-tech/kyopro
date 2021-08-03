n=int(input())
s=input()

dp = [0 for _ in range(7)]
md = 10 ** 9 + 7

for c in s: 
   i = 'atcoder'.find(c)
   if i == 0:
       dp[0] += 1
   if i >= 1:
       dp[i] += dp[i-1] % md

print(dp[6] % md)