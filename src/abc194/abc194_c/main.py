n = int(input())
a = list(map(int, input().split()))
print(len(a) * sum(map(lambda x: x ** 2, a)) - sum(a) ** 2)