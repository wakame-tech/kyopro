n = int(input())
a = [int(input()) - 1 for _ in range(n)]

def solve(a):
    c = 0
    cnt = 0
    while True:
        c = a[c]
        cnt += 1
        if c == 1:
            return cnt
        if cnt > len(a):
            break
    return -1

print(solve(a))