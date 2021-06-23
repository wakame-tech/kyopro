n, q = list(map(int, input().split()))

ans = [0 for i in range(n)]
for i in range(q):
    l, r, t = list(map(int, input().split()))
    for j in range(l - 1, r):
        ans[j] = t

for i in ans:
    print(i)
    
