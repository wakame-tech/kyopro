from collections import Counter

n = int(input())
s = [input() for i in range(n)]
ans = Counter(s)
for k in ['AC', 'WA', 'TLE', 'RE']:
    print(f'{k} x {ans.get(k) if ans.get(k) else 0}')