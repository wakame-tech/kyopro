a, b, k = list(map(int, input().split()))
for i in sorted(list(set([*list(range(a, min(a + k, b))), *list(range(max(a, b - k + 1), b + 1))]))):
    print(i)