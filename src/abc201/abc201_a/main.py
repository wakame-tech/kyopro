from itertools import permutations

def f(a):
    return a[2] - a[1] == a[1] - a[0]

a = map(int, input().split())
print('Yes' if any(map(f, permutations(a))) else 'No')