ss = [list(input()) for _ in range(3)]

def solve(ss):
    turn = list('abc').index(ss[0].pop(0))
    while True:
        if len(ss[turn]) == 0:
            return 'ABC'[turn]
        turn = list('abc').index(ss[turn].pop(0))

print(solve(ss))