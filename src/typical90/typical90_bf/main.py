n, k = list(map(int, input().split()))

def f(n):
    y = sum(map(int, list(str(n))))
    return (n + y) % (10 ** 5)

def solve(n):
    cyc = 0
    hist = set()
    x = n
    pre = -1
    while True:
        x = f(x)
        cyc += 1
        if cyc == k:
            res = [n]
            for _ in range(cyc):
                res.append(f(res[-1]))
            return 0, 10 ** 5, res
        if x in hist:
            pre = x
            break
        hist.add(x)

    hist = [pre]
    cnt = 0
    while n != pre:
        n = f(n)
        cnt += 1
        hist.append(f(hist[-1]))
    return cnt, cyc, hist

start, cyc, hist = solve(n)
i = (k - start) % (cyc - start)
# print(i)
ans = hist[0]
for _ in range(i):
    ans = f(ans)

print(ans)