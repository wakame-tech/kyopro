xs = list(map(int, list(input())))

def is_same(xs):
    for i in range(1, 4):
        if xs[0] != xs[i]:
            return False
    return True

def is_cont(xs):
    for i in range(1, 4):
        if xs[i] != (xs[i - 1] + 1) % 10:
            return False
    return True

print('Weak' if is_same(xs) or is_cont(xs) else 'Strong')