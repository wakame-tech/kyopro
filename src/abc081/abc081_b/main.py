n = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
    if any(map(lambda e: e % 2 == 1, a)):
        break
    a = list(map(lambda e: e // 2, a))
    ans += 1

print(ans)