a, b = map(int, input().split())
for i in range(1, 999 + 1):
    ha, hb = sum(range(i)), sum(range(i + 1))
    if ha - a == hb - b:
        print(ha - a)
        break