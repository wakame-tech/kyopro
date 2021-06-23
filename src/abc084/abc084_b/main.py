import re

a,b = list(map(int, input().split()))
s = input()

print('Yes' if re.match(r'^\d{' + str(a) + r'}\-\d{' + str(b) + r'}$', s) != None else 'No')