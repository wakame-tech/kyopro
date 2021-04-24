
import math
 
def solve(a, b):
    di = [0] * (b + 1)

    for s in range(1, b + 1):
        # div
        while i % 2 == 0:
            di[2] += 1
            i //= 2
        f = 3
        while f * f <= i:
            if i % f == 0:
                di[f] += 1
                i //= f
            else:
                f += 2
        if i != 1:
            di[i] += 1

        # for j in range(1, int(math.sqrt(i))):
        #     if i % j == 0:
        #         di[j] += 1
        #         if j != i // j:
        #             di[i // j] += 1

    for i in range(len(di) - 1, -1, -1):
        if di[i] > 1:
            return i
    return 1
 
a, b = map(int, input().split())
print(solve(a, b))