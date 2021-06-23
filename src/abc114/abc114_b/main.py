s = input()

d = 1000
for i in range(len(s) - 2):
    d = min(d, abs(int(s[i:i + 3]) - 753))

print(d)