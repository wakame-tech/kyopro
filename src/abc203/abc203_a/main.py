a = list(map(int, input().split()))
if len(set(a)) == 3:
    print(0)
else:
    if a[0] == a[1]:
        print(a[2])
    elif a[1] == a[2]:
        print(a[0])
    else:
        print(a[1])