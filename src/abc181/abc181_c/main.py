from itertools import combinations, permutations
n = int(input())
d = []
for i in range(n):
    x, y = map(int, input().split())
    d.append((x, y))

def is_same_line(ps):
    for p1, p2, p3 in permutations(ps, 3):
        if (p3[0] - p1[0]) * (p2[1] - p1[1]) == (p2[0] - p1[0]) * (p3[1] - p1[1]):
            return True
    return False

def solve(d):
    for ps in combinations(d, 3):
        if is_same_line(ps):
            return True
    return False

print('Yes' if solve(d) else 'No')           