a,b=list(map(int, input().split()))
if 0 < a and b == 0:
    print('Gold')
elif a == 0 and 0 < b:
    print('Silver')
else:
    print('Alloy')