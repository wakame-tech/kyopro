s = input()
k = int(input())

ans = {}
for i in range(len(s) - k + 1):
    substr = s[i:i + k]
    ans[substr] = True

print(len(ans))