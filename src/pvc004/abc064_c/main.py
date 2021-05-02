n = int(input())
a = map(int, input().split())

def color(rate):
    if rate <= 399:
        return 0
    if rate <= 799:
        return 1
    if rate <= 1199:
        return 2
    if rate <= 1599:
        return 3
    if rate <= 1999:
        return 4
    if rate <= 2399:
        return 5
    if rate <= 2799:
        return 6
    if rate <= 3199:
        return 7
    return 8

tourist = 0
cs = set()
for i in a:
    c = color(i)
    if c != 8:
        cs.add(c)
    else:
        tourist += 1

if tourist == n:
    print(1, len(cs) + tourist)
else:
    print(len(cs), len(cs) + tourist)