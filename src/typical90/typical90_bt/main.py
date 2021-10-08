import copy

ans = 0


def rec(w, h, m, l: int, flags: list, start: tuple, p: tuple):
    global ans
    flags[p[0] * w + p[1]] = True
    # print(p, l)
    for (y, x) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nex = (p[0] + y, p[1] + x)
        if 0 <= nex[0] < h and 0 <= nex[1] < w and m[nex[0]][nex[1]] == ".":
            # 特例
            if l > 1 and nex[0] == start[0] and nex[1] == start[1]:
                ans = max(ans, l + 1)
                return
            if not flags[nex[0] * w + nex[1]]:
                new_flags = copy.copy(flags)
                new_flags[nex[0] * w + nex[1]] = True
                rec(w, h, m, l + 1, new_flags, start, nex)

if __name__ == "__main__":
    h, w = list(map(int, input().split()))
    m = []
    for i in range(h):
        m.append(list(input()))

    for i in range(h):
        for j in range(w):
            flags = [False] * (w * h)
            s = [i, j]
            if m[s[0]][s[1]] == ".":
                rec(w, h, m, 0, flags, s, s)

    print(-1 if ans == 0 else ans)
