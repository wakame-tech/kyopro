x = int(input())

ans = 0
for b in range(1, 1000):
    for p in range(2, 11):
        if b ** p > x:
            break
        ans = max(ans, b ** p)

print(ans)