from collections import defaultdict

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

m = defaultdict(lambda: 0)
m[a[0]] += 1
s = e = 0
ans = 0
while s < n:
    # and 以降: len(m) <= k だと同じのが連続するときに追加できない
    while e < n - 1 and (len(m) != k or a[e + 1] in m):
        e += 1
        m[a[e]] += 1
        # print(f'+{a[e]} {len(m)}')

    # print(f'{s}..{e}')
    ans = max(ans, e - s + 1)

    _ = len(m)
    while s < n:
        m[a[s]] -= 1
        # print(f'-{a[s]}')
        if m[a[s]] == 0:
            del m[a[s]]
        s += 1
        if len(m) < _:
            break

print(ans)