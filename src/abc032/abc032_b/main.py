s = input()
k = int(input())

ans = set()
for i in range(len(s) - k):
    subs = s[i:i + k]
    ans.add(subs)

print(len(ans))