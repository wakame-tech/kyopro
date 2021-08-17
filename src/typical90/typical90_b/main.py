from itertools import product

n = int(input())

if n % 2 == 1:
    print('')
else:
    for s in product(['(', ')'], repeat = n):
        cnt = 0
        for j in range(n):
            if s[j] == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                break
        if cnt == 0:
            print(''.join(s))