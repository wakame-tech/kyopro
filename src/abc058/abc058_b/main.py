o = input()
e = input()
s = [e[i // 2] if i % 2 == 1 else o[i // 2] for i in range(len(o) + len(e))]
print(''.join(s))