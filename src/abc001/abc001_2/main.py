m = int(input())

if m < 100:
    print('00')
elif m <= 5000:
    m //= 100
    print(f'{m:02d}')
elif m <= 30000:
    m //= 1000
    print(f'{m + 50}')
elif m <= 70000:
    m //= 1000
    print(f'{(m - 30) // 5 + 80}')
else:
    print(89)