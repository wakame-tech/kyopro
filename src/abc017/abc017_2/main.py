x = input()

while True:
    if x == '':
        break
    if x.endswith('ch'):
        x = x[:-2]
    elif x.endswith('o'):
        x = x[:-1]
    elif x.endswith('k'):
        x = x[:-1]
    elif x.endswith('u'):
        x = x[:-1]
    else:
        break

print('YES' if x == '' else 'NO')