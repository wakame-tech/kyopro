n = int(input())
mx, j = 0, 0
for i in range(1, n):
    print(f'? 1 {i + 1}')
    d = int(input())
    if mx < d:
        mx = d
        j = i

for i in range(n):
    if i == j:
        continue
    print(f'? {j + 1} {i + 1}')
    mx = max(mx, int(input()))

print(f'! {mx}')