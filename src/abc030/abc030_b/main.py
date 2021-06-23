n, m = list(map(int, input().split()))
nd, md = ((n % 12) / 12) * 360, (m / 60) * 360
nd += md / 12
print(abs(nd - md))
