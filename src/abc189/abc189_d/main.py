n = int(input())
s = [input() for i in range(n)]

def debug(func):
    def inner(*args):
        res = func(*args)
        print(f'{args=} {res=}')
        return res
    return inner

# @debug
def cnt(k):
    global s
    if k == 0:
        return 1 if s[k] == 'AND' else 3
    if s[k] == 'AND':
        return min(2 ** (k + 1), cnt(k - 1))
    else:
        return 2 ** (k + 1) + cnt(k - 1)

print(cnt(n - 1))