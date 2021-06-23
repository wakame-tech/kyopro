n = int(input())
p = list(map(int, input().split()))
pp = list(range(1, n + 1))
print('YES' if sum(s != t for s, t in zip(p, pp)) <= 2 else 'NO')