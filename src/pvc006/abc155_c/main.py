from collections import Counter
from itertools import groupby

n = int(input())
ss = [input() for _ in range(n)]
ss.sort()
c = Counter(ss)

words = []
pret = c.most_common()[0][1]
for w, t in c.most_common():
    if pret == t:
        print(w)
    else:
        exit()
    pret = t