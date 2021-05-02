a, b = input().split()
a, b = int(a), int(b.replace('.', ''))
ans = str(a * b)
if int(ans) < 100:
    print(0)
else:
    print(ans[:-2])