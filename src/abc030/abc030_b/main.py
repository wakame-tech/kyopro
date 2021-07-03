# error
n, m = list(map(int, input().split()))
nd, md = ((n % 12) / 12) * 360, (m / 60) * 360
nd += md / 12
print(min(abs(nd - md), 360 - abs(nd - md)))