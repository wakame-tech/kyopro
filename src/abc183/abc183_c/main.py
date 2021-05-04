from itertools import permutations

n, k = map(int, input().split())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))

def cost(route, t):
    c = 0
    for i in range(1, len(route)):
        c += t[route[i - 1]][route[i]]
    c += t[route[-1]][route[0]]
    return c

ans = 0
for route in permutations(range(1, n), n - 1):
    c = cost([0, *route], t)
    if c == k:
        ans += 1

print(ans)