s, t = input(), int(input())
# p \pm mgn
p = complex(0)
k = 0

for c in s:
    if c == 'L':
        p -= 1
    elif c == 'R':
        p += 1
    elif c == 'U':
        p += 1j
    elif c == 'D':
        p -= 1j
    else:
        k += 1

def man_d(c: complex):
    return int(abs(c.real) + abs(c.imag))

if t == 1:
    cs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pest = list(p + complex(cx * k, cy * k) for cx, cy in cs)
    print(max(man_d(e) for e in pest))
else:
    while k > 0:
        if p.real > 0:
            p -= 1
        elif p.real < 0:
            p += 1
        elif p.imag > 0:
            p -= 1j
        elif p.imag < 0:
            p += 1j
        else:
            p += 1
        k -= 1

    print(man_d(p))