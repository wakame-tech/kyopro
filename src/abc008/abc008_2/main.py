from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
print(Counter(s).most_common()[0][0])