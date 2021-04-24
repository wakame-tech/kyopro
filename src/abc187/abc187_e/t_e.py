N = int(input())
edge = []
g = [list() for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge.append((A, B))
    g[A].append(B)
    g[B].append(A)
 
depth = [-1] * N
depth[0] = 0
q = [0]
while q:
    at = q.pop()
    for i in g[at]:
        if depth[i] == -1:
            depth[i] = depth[at] + 1
            q.append(i)
 
s = [0] * N
Q = int(input())
for i in range(Q):
    T, E, X = map(int, input().split())
    A, B = edge[E - 1]
    if depth[A] > depth[B]:
        A, B = B, A
        T ^= 3
    if T == 1:
        s[0] += X
        s[B] -= X
    else:
        s[B] += X

print(s)
print(depth)