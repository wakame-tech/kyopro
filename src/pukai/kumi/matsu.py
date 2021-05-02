n, m = map (int, input().split())
l = []
ll = [[0, m, 0]]

for i in range (2, n + 1):
    l = [0]
    for j in range (i):
        w = (ll[i - 2][j] + ll[i - 2][j + 1]) / 2 + m
        l.append (w)
    l.append (0)
    ll.append (l)

for k in range (n):
    ll[k] = list(filter (lambda x: x != 0 ,ll[k]))
    for q in range (len(ll[k])):
        ll[k][q] -= m

for p in range (n):
    ans = ' '.join([str(round(s)) for s in ll[p]])
    print (ans)