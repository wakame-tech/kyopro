a, b = list(map(int, input().split()))

ans = []
s = 0
i = 0
for i in range(500500, a + 500500):
    ans.append(i)
    s += i

for i in range(1, b + 1):
    ans.append(-i)
    s += -i

s -= ans.pop()
ans.append(-s)

print(*ans, sep=' ')