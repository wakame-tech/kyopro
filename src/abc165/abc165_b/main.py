x = int(input())
b = 100
i = 0
while True:
    b += b // 100
    i += 1
    if b >= x:
        break

print(i)