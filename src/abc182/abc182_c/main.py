from itertools import product

n = input()

def f(s, flags):
    return ''.join([s[i] for i in range(len(s)) if flags[i]])

ans = 19
for flags in product([True, False], repeat=len(n)):
    if all(map(lambda b: not b, flags)):
        continue

    k = f(n, flags)
    # print(flags, k)
    if int(k) % 3 == 0:
        ans = min(ans, len(n) - sum(flags))

print(-1 if ans == 19 else ans)