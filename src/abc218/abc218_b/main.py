p = list(map(int, input().split()))
for e in p:
  print(chr(e + ord('a') - 1), end = '')