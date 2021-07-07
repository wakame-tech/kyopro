n, k = list(map(int, input().split()))
d = list(map(int, input().split()))

while True:
    if all(int(c) not in d for c in str(n)):
        print(n)
        break
    n += 1