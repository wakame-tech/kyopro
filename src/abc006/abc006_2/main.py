n = int(input())
ans = 0
if n < 3:
    print([0, 0, 1][n - 1])
else:
    pre, prepre, preprepre = 0, 0, 1
    for i in range(n - 2):
        ans = pre + prepre + preprepre
        preprepre = prepre
        prepre = pre
        pre = ans
    print(ans % 10007)