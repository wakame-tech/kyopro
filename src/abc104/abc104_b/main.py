s = input()

print('AC' if s[0] == 'A' and s[2:-1].count('C') == 1 and sum(map(lambda c: ord('a') <= ord(c) <= ord('z'), s)) == len(s) - 2 else 'WA')