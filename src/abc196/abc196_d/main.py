import copy

h, w, max_a, max_b = list(map(int, input().split()))
cnt = 0

def dfs(tatami: list, pos: int, h: int, w: int, a: int, b: int):
    def dbg(tatami: list):
        for i in range(h):
            for j in range(w):
                print('#' if tatami[i * h + j] else '.', end='')
            print()
        print()

    global max_a, max_b, cnt

    # print(f'start {pos}')

    if a == max_a and b == max_b and all(tatami):
        # print('+1')
        cnt += 1
        return

    if pos == h * w:
        return

    if b < max_b and not tatami[pos]:
        # square
        # print(f'square@{pos}')
        # dbg(tatami)
        _tatami = copy.copy(tatami)
        _tatami[pos] = True
        # dbg(_tatami)

        dfs(_tatami, pos + 1, h, w, a, b + 1)

    if a < max_a and pos % w != w - 1 and (not tatami[pos] and not tatami[pos + 1]):
        # horizontal
        # print(f'horizontal@{pos}')
        # dbg(tatami)
        _tatami = copy.copy(tatami)
        _tatami[pos] = _tatami[pos + 1] = True
        # dbg(_tatami)

        dfs(_tatami, pos + 1, h, w, a + 1, b)
    if a < max_a and pos < h * w - w and (not tatami[pos] and not tatami[pos + w]):
        # vertical
        # print(f'vertical@{pos}')
        # dbg(tatami)
        _tatami = copy.copy(tatami)
        _tatami[pos] = _tatami[pos + w] = True
        # dbg(_tatami)

        dfs(_tatami, pos + 1, h, w, a + 1, b)
    else:
        dfs(tatami, pos + 1, h, w, a, b)

    # print(f'end {pos}')

tatami = [False for _ in range(h * w)]
dfs(tatami, 0, h, w, 0, 0)
print(cnt)