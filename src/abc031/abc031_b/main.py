l, h = list(map(int, input().split()))
n = int(input())
a = [int(input()) for _ in range(n)]

for i in a:
    if i < l:
        print(l - i)
    elif i <= h:
        print(0)
    else:
        print(-1)
        