# TODO
k, s, t = [input() for i in range(3)]
k = int(k)

def score(s: str):
    d = [0 for _ in range(9)]
    for c in s:
        if c == '#':
            continue
        d[int(c) - 1] += 1
    return sum(i * 10 ** d[i - 1] for i in range(1, 10))


def cumsum_right(arr):
    cs = [0] * len(arr)
    cs[-1] = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        cs[i] = cs[i + 1] + arr[i]
    return cs

def deck(k, s, t):
    # 残りカードで i 番目より右にある数の合計を返す
    d = [k for _ in range(9)]
    for c in s[:-1]:
        d[int(c) - 1] -= 1
    for c in t[:-1]:
        d[int(c) - 1] -= 1

    print(d)
    cs = cumsum_right(d)
    print(cs)
    return cs

print(t, s)
delta = score(t) - score(s)
print(deck(k, s, t))
print(delta)