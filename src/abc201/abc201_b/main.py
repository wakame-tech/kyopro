n = int(input())
l = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    l.append((s, t))

l.sort(key=lambda e: e[1], reverse=True)
print(l[1][0])