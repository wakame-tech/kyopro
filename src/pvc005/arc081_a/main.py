n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

prenum, pre, cnt = 0, 0, a[-1]
for e in a:
    if e != pre:
        if cnt >= 2:
            prenum = pre
        cnt = 0

    cnt += 1

    if cnt == 4:
        print(e ** 2)
        exit()
    if prenum != 0 and cnt == 2:
        print(prenum * e)
        exit()

    if cnt >= 2:
        prenum = e

    pre = e
else:
    print(0)