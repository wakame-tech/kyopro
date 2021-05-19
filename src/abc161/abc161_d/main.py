from collections import deque

def debug(func):
    def inner(*args):
        print(f'[@debug] {func.__name__}{args} = ', end='')
        res = func(*args)
        print(f'{res}')
        return res
    return inner

# @debug
def succ(x: deque) -> deque:
    if len(x) == 1:
        return deque(str(int(''.join(x)) + 1))
        
    i = len(x) - 2
    x[i + 1] = str(int(x[i + 1]) + 1)

    while i >= 0:
        if int(x[i + 1]) == int(x[i]) + 2 or int(x[i + 1]) > 9:
            # carry
            x[i] = str(int(x[i]) + 1)
            for j in range(i + 1, len(x)):
                x[j] = str(max(0, int(x[j - 1]) - 1))
        else:
            break

        i -= 1

    if int(x[0]) > 9:
        for i in range(len(x)):
            x[i] = '0'
        x.appendleft(str(1))
    
    return x

def solve(k):
    x = '0'
    for i in range(k):
        x = succ(deque(x))

    return int(''.join(x))

# def answer(k):
#     x = 0
#     for i in range(k):
#         while True:
#             x += 1
#             flg = True

#             for i in range(1, len(str(x))):
#                 if abs(int(str(x)[i]) - int(str(x)[i - 1])) > 1:
#                     flg = False
#                     break
#             if flg:
#                 break
#     return x

k = int(input())
print(solve(k))