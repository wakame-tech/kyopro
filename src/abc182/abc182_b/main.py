n = int(input())
a = list(map(int, input().split()))

max_gcdd, max_k = 0, 0
for k in range(2, 1001):
    gcdd = len([True for e in a if e % k == 0])
    if gcdd > max_gcdd:
        max_gcdd = gcdd
        max_k = k

print(max_k)