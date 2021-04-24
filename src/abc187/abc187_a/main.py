a, b = input().split(' ')

def f(s):
  return sum(map(int, s))
print(max(f(a), f(b)))