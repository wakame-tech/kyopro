n = int(input())

def solve(n):
    if n < 10:
        print(0)
    else:
        k = len(str(n)) // 2
        # n: strstr -> k * 10 ** (n // 2) + k
        t = int(str(n)[0:k])
        return t if t <= int(str(n)[k:]) else t - 1

print(solve(n))