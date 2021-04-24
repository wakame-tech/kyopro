n = int(input())
s = [c for c in input()]
# R...W... にする
# op1. Wを後ろに
# op2. WをRに

cnt = 0
wi, ri = 0, n - 1

while True:
    while wi != n and s[wi] != "W":
        wi += 1
    while ri != 0 and s[ri] != "R":
        ri -= 1
    if wi >= ri:
        break
    # print(f"{wi} {ri}")
    s[wi], s[ri] = s[ri], s[wi]
    wi += 1
    ri -= 1
    cnt += 1

# print(s)
print(cnt)