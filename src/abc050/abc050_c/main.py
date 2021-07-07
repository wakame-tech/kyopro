n = int(input())
a = list(map(int, input().split()))
a.sort()
aa = [abs(i - (n - i - 1)) for i in range(n)]
aa.sort()

if all(ai == aai for ai, aai in zip(a, aa)):
    print((2 ** (n // 2) % (10 ** 9 + 7)))
else:
    print(0)