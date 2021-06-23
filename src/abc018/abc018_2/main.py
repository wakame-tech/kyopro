s = list(input())
n = int(input())
for i in range(n):
    l, r = list(map(int, input().split()))
    l, r = l - 1, r - 1
    s[l:r + 1] = s[l:r + 1][::-1]

print("".join(s))
