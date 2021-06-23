s = input()

print('Yes' if all(s[i] in 'RUD' if i % 2 == 0 else s[i] in 'LUD' for i in range(len(s))) else 'No')