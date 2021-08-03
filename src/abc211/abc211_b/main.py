s = [input() for i in range(4)]
d = {}
for i in range(4):
    d[s[i]] = True

print('Yes' if 'H' in d and '2B' in d and '3B' in d and 'HR' in d else 'No')