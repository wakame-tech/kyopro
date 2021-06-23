n, l = list(map(int, input().split()))
s = [input() for i in range(n)]
s.sort()

print(''.join(s))