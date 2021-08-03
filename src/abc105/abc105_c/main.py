# TODO: solve
n=int(input())

ans = ''
while abs(n) != 1:
    if n < 0:
        d, m = divmod(n - 1, -2)
        m += 1
        print(f'{n=} % -2 = {d=} ... {m=}')
        ans = str(m) + ans
        n = d
    else:
        d, m = divmod(n - 1, -2)
        m += 1
        print(f'{n=} % -2 = {d=} ... {m=}')
        ans = str(m) + ans
        n = d

ans = str(n) + ans

print(ans)