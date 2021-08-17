n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

cs = [0]
for i in range(n):
    cs.append(cs[i] + s[i])


ans = []
# print(cs)
t0 = [t[i] + (cs[-1] - cs[i]) for i in range(n)]
# print(t0)
m = min(t0)

for i in range(n):
    print(min(t[i], m + cs[i]))