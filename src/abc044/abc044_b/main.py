w = input()
cnts = [0 for i in range(26)]
for c in w:
    cnts[ord(c) - ord("a")] += 1

print("Yes" if all(map(lambda e: e % 2 == 0, cnts)) else "No")
