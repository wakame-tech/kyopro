s, t = input(), input()


def l(a, b):
    return sum([ca != cb for (ca, cb) in zip(a, b)])


m = len(s)
if s == t:
    print(0)
    exit()

for i in range(len(s) - len(t) + 1):
    mi = l(s[i : i + len(t)], t)
    # print(f"{s[i:i + len(t)]} {t}: {mi}")
    m = min(m, mi)
print(m)