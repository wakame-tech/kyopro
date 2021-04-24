# n = int(input())
# h = {}
# for i in range(n):
#     a = int(input())
#     if a in h:
#         del h[a]
#     else:
#         h[a] = True

# print(len(h))

n = int(input())
h = set()
for i in range(n):
    a = int(input())
    if a in h:
        h.remove(a)
    else:
        h.add(a)

print(len(h))