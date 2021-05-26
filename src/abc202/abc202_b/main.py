s = input()

for c in s[::-1]:
    c = {
        '0': 0,
        '1': 1,
        '8': 8,
        '6': 9,
        '9': 6
    }[str(c)]
    print(c, end='')