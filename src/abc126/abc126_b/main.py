s = input()
a, b = int(s[:2]), int(s[2:])
am, bm = 1 <= a <= 12, 1 <= b <= 12
if am and bm:
    print('AMBIGUOUS')
elif am and not bm:
    print('MMYY')
elif not am and bm:
    print('YYMM')
else:
    print('NA')