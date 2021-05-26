from collections import deque

def ncr(n: int, r: int) -> int:
    """
    nCr
    """
    assert(n >= r)
    res = 1
    for i in range(n, n - r, -1):
        res *= i
    for i in range(r, 0, -1):
        res //= i
    return res

def solve(a, b, k):
    ans, s, e, border = '', 0, ncr(a + b, a) - 1, 0
    while a != 0 and b != 0:
        border = s + ncr(a - 1 + b, a - 1)
        # print(f'({k}, {a}, {b}), 0: {a - 1 + b}C{a - 1} = {ncr(a - 1 + b, a - 1)}, {s}..<{border}, {border}..{e} => {"a" if k < border else "b"}?')
        if k < border:
            ans += 'a'
            a -= 1
            e = border
        else:
            ans += 'b'
            b -= 1
            s = border

    ans += 'a' * a + 'b' * b
    return ans

a, b, k = list(map(int, input().split()))
print(solve(a, b, k - 1))