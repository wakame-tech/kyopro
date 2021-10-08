n=int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)
ans = x // sum_a
s = sum_a * ans
ai = ans * n
# print(s, ai)
for i in range(n):
    s += a[i]
    ai += 1
    if s > x:
        print(ai)
        break