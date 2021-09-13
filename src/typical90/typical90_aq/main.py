from collections import deque

h, w = list(map(int, input().split()))
rs, cs = list(map(int, input().split()))
rt, ct = list(map(int, input().split()))
g = []
for i in range(h):
    g.append(input())


def dire2pos(dire):
    if dire == 0:
        return [0, -1]
    elif dire == 1:
        return [1, 0]
    elif dire == 2:
        return [0, 1]
    else:
        return [-1, 0]

def bfs(g, w, h, start, goal):
    inf = 10 ** 6
    dires = list(range(4))
    costs = [[[inf, inf, inf, inf] for _ in range(w)] for _ in range(h)]

    # pos, dire
    q = deque()
    costs[start[1]][start[0]] = [0, 0, 0, 0]
    for d in dires:
        q.append((start, d))

    while q:
        pos, predire = q.popleft()

        for dire in dires:
            nd = dire2pos(dire)
            newpos = (pos[0] + nd[0], pos[1] + nd[1])

            if not (0 <= newpos[0] < w) or not (0 <= newpos[1] < h):
                continue
            # print(newpos)
            if g[newpos[1]][newpos[0]] == "#":
                continue

            cost = costs[pos[1]][pos[0]][predire] + (1 if dire != predire else 0)
            if cost < costs[newpos[1]][newpos[0]][dire]:
                costs[newpos[1]][newpos[0]][dire] = cost
                if dire == predire: # same dire
                    q.appendleft((newpos, dire))
                else: # differnt dire
                    q.append((newpos, dire))

    return min(costs[goal[1]][goal[0]])

print(bfs(g, w, h, (cs - 1, rs - 1), (ct - 1, rt - 1)))
