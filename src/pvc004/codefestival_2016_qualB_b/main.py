n, a, b = map(int, input().split())
s = input()

ia, ib = 0, 0
for c in s:
    if c == 'a':
        ia += 1
    if c == 'b':
        ib += 1

passed = 0
flim = b
for i in range(n):
    if s[i] == 'a':
        if passed < a + b:
            print('Yes')
            passed += 1
            continue
    if s[i] == 'b':
        flim -= 1
        if passed < a + b and flim >= 0:
            print('Yes')
            passed += 1
            continue
    print('No')