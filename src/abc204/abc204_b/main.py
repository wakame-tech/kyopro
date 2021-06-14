n = int(input())
a = list(map(int, input().split()))
print(sum(map(lambda e: 0 if e <= 10 else e - 10, a)))