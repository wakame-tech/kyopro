from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
m = []
flags = [[False for _ in range(c)] for __ in range(r)]
for i in range(r):
    m.append(input())

def bfs(m, flags, start, goal):
    q = deque()
    q.append((start, 0))
    while len(q) != 0:
        n, d = q.popleft()
        for dr in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            p = (n[0] + dr[0], n[1] + dr[1])
            if flags[p[1]][p[0]] or m[p[1]][p[0]] == '#':
                continue
            if p == goal:
                return d + 1
            q.append((p, d + 1))
            flags[p[1]][p[0]] = True 

print(bfs(m, flags, (sx - 1, sy - 1), (gx - 1, gy - 1)))