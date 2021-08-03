n, k = list(map(int, input().split()))
s = input()

table = [[0 for x in range(n)] for y in range(26)]

idx = [-1 for _ in range(26)]
for i in range(n - 1, -1, -1):
    # print(f'[{i}] = {s[i]}')
    idx[ord(s[i]) - ord("a")] = i + 1
    for j in range(26):
        table[j][i] = idx[j]

ans = ""
cur = 0
for j in range(k):
    # print(f"cur = {cur}, ans = {ans}")
    for i in range(26):
        # print(n, (k - j - 1))
        if 0 < table[i][cur] <= n - (k - j - 1):
            c = chr(ord("a") + i)
            # print(c)
            ans += c
            cur = table[i][cur]
            break

print(ans)