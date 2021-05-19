sx, sy, gx, gy = list(map(int, input().split()))

# (sx, -sy) (gx, gy)
# l = (gy + sy) / (gx - sx)
# y = l(x - gx) + gy | y = 0
# <=> -gy / l + gx = x
print(-gy / ((gy + sy) / (gx - sx)) + gx)