n=int(input())
his = set()
for i in range(n):
    s,t=list(map(str, input().split()))
    his.add((s, t))

print('No' if len(his) == n else 'Yes')