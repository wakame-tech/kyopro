n = int(input())

def intersect(p1, p2):
    s1, e1 = p1
    s2, e2 = p2
    res = s1 <= s2 <= e1 or s1 <= e2 <= e1 or s2 <= s1 <= e2 or s2 <= e1 <= e2
    # print(f'{p1[0]}-{p1[1]} & {p2[0]}-{p2[1]} = {res}')
    return res

ans = 0
qs = []
for i in range(n):
    t, l, r = list(map(int, input().split()))
    if t == 3 or t == 4:
        l += 0.1
    if t == 2 or t == 4:
        r -= 0.1
    qs.append((l, r))

for i in range(n):
    for j in range(i + 1, n):
        if intersect(qs[i], qs[j]):
            ans += 1

print(ans)