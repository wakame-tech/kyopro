sx, sy, tx, ty = list(map(int, input().split()))

def move(s, t, iki):
    if iki:
        return 'U' * (t[1] - s[1]) + 'R' * (t[0] - s[0])
    else:
        return 'D' * (t[1] - s[1]) + 'L' * (t[0] - s[0])

ans = ''
ans += move((sx, sy), (tx, ty), True)
ans += move((sx, sy), (tx, ty), False)
ans += 'L'
ans += move((sx - 1, sy), (tx, ty + 1), True)
ans += 'D'
ans += 'R'
ans += move((sx, sy - 1), (tx + 1, ty), False)
ans += 'U'
print(ans)