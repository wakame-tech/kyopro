s = input()

print('Yes' if sum([int(c) for c in s]) % 9 == 0 else 'No')