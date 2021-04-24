s = input()
ai, zi = s.index('A'), len(s) - list(reversed(s)).index('Z')
print(zi - ai)