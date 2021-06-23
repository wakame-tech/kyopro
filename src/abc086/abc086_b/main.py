a, b = list(map(int, input().split()))
c = int(str(a) + str(b))

def is_sq(c):
    for i in range(101):
        if c == i ** 2:
            return True
    return False

print('Yes' if is_sq(c) else 'No')