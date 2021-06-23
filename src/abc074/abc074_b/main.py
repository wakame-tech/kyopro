n = int(input())
k = int(input())
x = list(map(int, input().split()))

print(sum(map(lambda xi: min(k - xi, xi) * 2, x)))