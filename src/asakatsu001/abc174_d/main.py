n, s = int(input()), list(input())

def solve(n, s):
    cnt = 0
    w, r = 0, n - 1

    while True:
        # first w
        while w != n and s[w] != "W":
            w += 1
        # last r
        while r != 0 and s[r] != "R":
            r -= 1

        if w >= r:
            return cnt
            
        # swap
        s[w], s[r] = s[r], s[w]
        
        w += 1
        r -= 1
        cnt += 1

print(solve(n, s))