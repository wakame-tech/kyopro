# 14:00
def detect_cycles(a):
    cycles = []
    hist = set()
    pre = 0
    start = 0
    while True:
        if a[pre] - 1 in hist:
            start = cycles.index(a[pre] - 1)
            break
        cycles.append(a[pre] - 1)
        hist.add(a[pre] - 1)
        pre = a[pre] - 1

    return cycles, start, len(cycles) - 1

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    cycles, start, end = detect_cycles(a)
    # print(cycles, start, end)

    if k <= len(cycles):
        print(cycles[k - 1] + 1)
    else:
        mod = (k - start - 1) % (end - start + 1)
        print(cycles[start + mod] + 1)