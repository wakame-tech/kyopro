n = int(input())
a = list(map(int, input().split()))
m = 10 ** 9 + 7
s, t = sum(a), sum(i ** 2 for i in a)
print(((s ** 2 - t) // 2) % m)