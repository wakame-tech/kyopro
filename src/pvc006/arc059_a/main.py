n = int(input())
a = list(map(int, input().split()))

score = 10 ** 6
for i in range(-100, 101):
    s = sum([(abs(i - j) ** 2) for j in a])
    score = min(score, s)

print(score)