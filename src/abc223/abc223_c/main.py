import bisect

# 1D cumsum
class CumSum1D:
    def __init__(self, arr: list):
        self.s = [0]
        l = len(arr)
        for i in range(l):
            self.s.append(self.s[i] + arr[i])

    def sum(self, s: int, e: int) -> int:
        """ [s, e) """
        return self.s[e] - self.s[s]

n = int(input())
lens, times, speeds = [], [], []
for i in range(n):
    a, b = list(map(int, input().split()))
    lens.append(a)
    times.append(b)
    speeds.append(a / b)

lens_sum = CumSum1D(lens)
times_sum = CumSum1D(times)
speeds_sum = CumSum1D(speeds)

t = speeds_sum.s[-1] / 2
# print(f't = {t}')
i = bisect.bisect_right(speeds_sum.s, t)
dt = t - speeds_sum.s[i - 1]
# print(f'dt = {dt}')
# print(f'{lens_sum.s[i - 1]}, {lens[i - 1]}, {dt}, {times[i - 1]}')
ans = lens_sum.s[i - 1] +  dt * times[i - 1]
print(ans)
