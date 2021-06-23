n, a, b = list(map(int, input().split()))
x = 0
for i in range(n):
    s, d = input().split()
    d = int(d)
    d = max(a, min(b, d))
    x += -d if s == 'West' else d

if x < 0:
    print(f'West {abs(x)}')
elif x > 0:
    print(f'East {x}')
else:
    print(0)