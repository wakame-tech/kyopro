from itertools import product

n, m = map(int, input().split())
dishes = []
for i in range(m):
    a, b = map(int, input().split())
    dishes.append((a, b))

k = int(input())
choices = []
for i in range(k):
    c, d = map(int, input().split())
    choices.append((c, d))

ans = 0
for choice in product(*choices):
    choice = set(choice)
    a = sum(dish[0] in choice and dish[1] in choice for dish in dishes)
    ans = max(ans, a)

print(ans)