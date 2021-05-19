a, b, w = map(int, input().split())
w *= 1000

for i in range(1000 * 1000 + 1):
    if i * a <= w <= i * b:
        print(i)
        break
else:
    print('UNSATISFIABLE')
    exit()

for i in range(1000 * 1000 + 1)[::-1]:
    if i * a <= w <= i * b:
        print(i)
        break
else:
    print('UNSATISFIABLE')
