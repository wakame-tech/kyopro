from collections import deque

def swap(s, i, j):
    ret = list(s)
    ret[i], ret[j] = ret[j], ret[i]
    return ''.join(ret)

def bfs(g, start, goal):
    dists = {}
    q = deque()
    q.append(start)
    dists[start] = 0

    while q:
        s = q.popleft()
        i = s.index('8')
        for j in g[i]:
            t = swap(s, i, j)
            if t in dists:
                continue
            dists[t] = dists[s] + 1
            q.append(t)
    
    if goal not in dists:
        return -1
    else:
        return dists[goal]

if __name__ == "__main__":
    m = int(input())
    g = [[] for _ in range(9)]
    for i in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    p = list(map(int, input().split()))

    s = ['8'] * 9
    for i in range(len(p)):
        s[p[i] - 1] = str(i)
    s = ''.join(s)
    print(bfs(g, s, '012345678'))