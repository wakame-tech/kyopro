from math import factorial

s = input()

def sat(i, cond):
    for k, c in enumerate(i):
        for j in range(10):
            if s[j] == 'o' and str(j) not in i:
                return False
            if s[j] == 'x' and str(j) in i:
                return False

    return True

ans = 0
for i in range(10000):
    i = str(i).zfill(4)
    if sat(i, s):
        ans += 1

print(ans)