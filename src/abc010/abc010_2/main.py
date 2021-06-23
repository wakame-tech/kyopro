n = int(input())
a = list(map(int, input().split()))
ans = 0
anss = [0, 1, 0, 3, 2, 1, 0, 1]
for e in a:
    ans += anss[(e - 1) % 8]

print(ans)