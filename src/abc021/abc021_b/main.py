n = int(input())
a, b = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
p = [a, *p, b]
print('YES' if len(set(p)) == len(p) else 'NO')