n, k = map(int, input().split())
c = list(map(int, input().split()))
ans = []
dic = {}
for i in c[0:k]:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# print(dic)
ans.append(len(dic))
for i in range(n - k):
    dic[c[i]] -= 1
    if dic[c[i]] == 0:
        if c[i + k] in dic:
            ans.append(ans[-1] - 1)
            dic[c[i + k]] += 1
        else:
            ans.append(ans[-1])
            dic[c[i + k]] = 1
    else:
        if c[i + k] in dic:
            ans.append(ans[-1])
            dic[c[i + k]] += 1
        else:
            ans.append(ans[-1] + 1)
            dic[c[i + k]] = 1
print(max(ans))
