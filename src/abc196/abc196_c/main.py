n = int(input())

def solve(n):
    k = len(str(n)) // 2

    cnt = 0
    for i in range(1, 10 ** (k + 1)):
        if int(str(i) * 2) <= n:
            cnt += 1

    return cnt

print(solve(n))