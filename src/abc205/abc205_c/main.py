a, b, c = list(map(int, input().split()))

def solve(a, b, c):
    if a == b or (c % 2 == 0 and abs(a) == abs(b)):
        return '='
    if c % 2 == 1:
        if a <= 0 and b >= 0:
            return '<'
        else:
            return '>'
    if c % 2 == 0:
        if abs(a) < abs(b):
            return '<'
        else:
            return '>'

print(solve(a, b, c))

# assert(solve(-2, 2, 2) == '=')
# assert(solve(2, -1, 3) == '>')
# assert(solve(2, 3, 2) == '<')
# assert(solve(3, 2, 2) == '>')
# assert(solve(-3, 3, 2) == '=')
# assert(solve(-3, 3, 3) == '<')
# assert(solve(-2, -3, 2) == '<')
# assert(solve(-2, -3, 3) == '>')
# assert(solve(0, 0, 1) == '=')
# assert(solve(0, 3, 1) == '<')