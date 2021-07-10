# TODO: submit
n = int(input())
a = list(map(int, input().split()))
a.sort()

d = set()
ans = 0
for e in a:
    if e not in d:
        ans += 1
    k = 0
    while e * 2 ** k < 10 ** 9:
        d.add(e * 2 ** k)
        k += 1

print(ans)