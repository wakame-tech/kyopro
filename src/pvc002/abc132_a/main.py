s = input()
d = {}
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print('Yes' if all(map(lambda e: e == 2, dict.values(d)))else 'No')