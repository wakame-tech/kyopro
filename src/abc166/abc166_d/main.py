import copy

x = int(input())

def solve(x):
    limit = 3
    rng = range(-10 ** limit, 10 ** limit)
    for a in copy.copy(rng):
        for b in copy.copy(rng):
            if a ** 5 - b ** 5 == x:
                return a, b


print(*solve(x))
