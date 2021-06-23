h,w = list(map(int, input().split()))
c = [input() for _ in range(h)]

for i in range(h * 2):
    print(c[i // 2])