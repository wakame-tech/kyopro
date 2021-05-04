n = int(input())
t, a = map(int, input().split())
h = [(i, x) for i, x in enumerate(map(int, input().split()))]
print(min(h, key=lambda tup: abs(a - (t - tup[1] * 0.006)))[0] + 1)