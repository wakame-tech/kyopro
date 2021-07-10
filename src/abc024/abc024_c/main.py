# TODO: submit
n, d, k = list(map(int, input().split()))
ranges = []
for i in range(d):
    l, r = list(map(int, input().split()))
    ranges.append((l, r))

towns = []
for i in range(k):
    s, t = list(map(int, input().split()))
    towns.append((s, t))

for i in range(k):
    s, t = towns[i][0], towns[i][1]
    _l, _r = s, s
    for j in range(n):
        l, r = ranges[j][0], ranges[j][1]
        if l <= _l <= r:
            _l = min(_l, l)
        if l <= _r <= r:
            _r = max(_r, r)

        if _l <= min(s, t) and max(s, t) <= _r:
            print(j + 1)
            break