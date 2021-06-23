n = int(input())
s = input()
if n % 2 == 0:
    print('Yes' if s[:n // 2] == s[n // 2:] else 'No')
else:
    print('No')