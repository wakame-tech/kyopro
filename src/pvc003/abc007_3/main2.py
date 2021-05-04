from collections import deque

h, w = map(int, input().split())
sy, sx = map(int, input().split())
start = (sx - 1, sy - 1)
gy, gx = map(int, input().split())
goal = (gx - 1, gy - 1)
grid = []
for i in range(h):
    grid.append(input())

def bfs(states, w: int, h: int, start, goal):
    flags = [[False for _ in range(w)] for __ in range(h)]
    q = deque()
    # init
    q.append((start, 0))

    def nexts(cur):
        drs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(cur[0] + dr[0], cur[1] + dr[1]) for dr in drs]

    while len(q) != 0:
        cur, d = q.popleft()
        # nexts
        for nxt in nexts(cur):
            if flags[nxt[1]][nxt[0]] or states[nxt[1]][nxt[0]] == '#':
                continue
            if nxt == goal:
                return d + 1
            q.append((nxt, d + 1))
            flags[nxt[1]][nxt[0]] = True

print(bfs(grid, w, h, start, goal))