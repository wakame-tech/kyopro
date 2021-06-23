n = int(input())
s = input().split()
print('Three' if len(set(list(s))) == 3 else 'Four')