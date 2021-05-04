n, x = map(int, input().split())
a = map(int, input().split())

for el in a:
    if el == x:
        continue
    print(f'{el} ', end='')