import math

n = int(input())

def ton(v, n = 26):
    def f(i):
        if i == 0:
            return ''
        else:
            return chr(ord('a') + i)

    res = []
    while v >= n:
        r = (v + n) % n
        res.append(f(r))
        v //= n

    if len(res) == 0:
        res.append(f(v))
    else:
        res.append(f(v - 1))

    return ''.join(res[::-1])

print(ton(n - 1))