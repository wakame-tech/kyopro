x = input()
n = int(input())
ss = [input() for _ in range(n)]

xmp = { c: chr(ord('a') + i) for i, c in enumerate(x) }

# print(xmp)

def dec(s):
  return ''.join(xmp[c] for c in s)

ss.sort(key=lambda s: dec(s))

for s in ss:
  print(s)