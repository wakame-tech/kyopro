n = int(input())
b = [-1]
for i in range(n - 1):
    b.append(int(input()) - 1)


def salary(n, i, b):
    bs = []
    for j in range(n):
        if b[j] == i:
            bs.append(j)

    if len(bs) == 0:
        return 1
    else:
        bs_salary = list(map(lambda e: salary(n, e, b), bs))
        return max(bs_salary) + min(bs_salary) + 1


print(salary(n, 0, b))