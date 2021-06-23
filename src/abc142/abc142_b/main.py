n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

print(sum(map(lambda e: e >= k, h)))