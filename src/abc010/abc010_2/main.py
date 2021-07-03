n = int(input())
a = list(map(int, input().split()))
ans = 0
# i % 2 == 0 & i % 3 != 1, ∃k where (i - k) % 2 == 0 & (i - k) % 3 != 1
anss = [0, 1, 0, 1, 2, 3, 0, 1]
for e in a:
    ans += anss[(e - 1) % 8]

print(ans)