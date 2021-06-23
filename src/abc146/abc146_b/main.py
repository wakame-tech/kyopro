n = int(input())
s = input()

print(''.join(chr(ord('A') + (((ord(c) - ord('A')) + n) % 26)) for c in s))