n = int(input())

s = 0
i = 1
while True:
    s += i
    if s >= n:
        break

    i += 1

print(i)