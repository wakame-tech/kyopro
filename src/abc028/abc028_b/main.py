s = input()
ans = [0 for _ in range(6)]
for c in s:
    ans[ord(c) - ord('A')] += 1

print(*ans)