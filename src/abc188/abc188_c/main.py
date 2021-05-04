n = int(input())
a = map(int, input().split())
ai = [(a, i) for i, a in enumerate(a, start=1)]
m1 = max(ai[:len(ai) // 2], key=lambda x: x[0])
m2 = max(ai[len(ai) // 2:], key=lambda x: x[0])
print(min([m1, m2], key=lambda x: x[0])[1])