n = int(input())
stk = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a == b:
        stk += 1
    else:
        stk = 0
    if stk >= 3:
        break

print('Yes' if stk >= 3 else 'No')