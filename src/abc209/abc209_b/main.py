n,x=list(map(int, input().split()))
a=list(map(int, input().split()))

sm = 0
for i in range(n):
    if i % 2 == 0:
        sm += a[i]
    else:
        sm += a[i] - 1

print('Yes' if sm <= x else 'No')