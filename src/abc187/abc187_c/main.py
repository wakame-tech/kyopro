n = int(input())
dic = {}
ss = []
for i in range(n):
  ss.append(input())
for s in ss:
  i = 1 if s[0] == '!' else 0
  if s[i:] in dict.keys(dic) and dic[s[i:]] != s:
    print(s[i:])
    exit()

  dic[s[i:]] = s

print('satisfiable')