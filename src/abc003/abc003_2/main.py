s, t = input(), input()

def solve(s, t):
    for si, ti in zip(s, t):
        if si == '@' and ti == '@':
            continue
        elif si == '@':
            if ti in 'atcoder':
                continue
            return False
        elif ti == '@':
            if si in 'atcoder':
                continue
            return False
        elif si != ti:
            return False
    return True

print('You can win' if solve(s, t) else 'You will lose')