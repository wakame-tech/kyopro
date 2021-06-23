x = int(input())

def solve(x):
    for i in range(1000):
        if i ** 4 == x:
            return i

print(solve(x))