# 14:00 - 14:20
n, m, q = list(map(int, input().split()))
st = []
for i in range(n):
    w, v = list(map(int, input().split()))
    st.append((w, v))
x = list(map(int, input().split()))
qs = []
for i in range(q):
    l, r = list(map(int, input().split()))
    qs.append((l, r))

dp = [0 for w in range(10 ** 1)]
for i in range(1, len(dp)):
    dp[i] = max(dp[i - 1], )