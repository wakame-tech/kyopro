from itertools import permutations

n = int(input())
ps = ''.join(map(lambda i: str(int(i) - 1), input().split()))
qs = ''.join(map(lambda i: str(int(i) - 1), input().split()))

dic = [''.join(map(str, p)) for p in permutations(range(n))]
print(abs(dic.index(ps) - dic.index(qs)))