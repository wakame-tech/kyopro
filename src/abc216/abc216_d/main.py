import sys
def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(10 ** 6)


def scc(n: int, g, g_t):
    order = []
    visited = [False] * n
    group_indice = [None] * n

    def dfs(s):
        visited[s] = True
        for t in g[s]:
            if not visited[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, cnt):
        group_indice[s] = cnt
        visited[s] = True
        for t in g_t[s]:
            if not visited[t]:
                rdfs(t, cnt)

    # step 1. 帰りがけ順に順番を記録
    for i in range(n):
        if not visited[i]:
            dfs(i)

    visited = [0] * n
    cnt = 0

    # step 2. 後に記録した頂点からDFS
    for s in reversed(order):
        if not visited[s]:
            rdfs(s, cnt)
            cnt += 1

    return cnt, group_indice


def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    g_t = [[] for _ in range(n)]
    for i in range(m):
        k = int(input())
        a = list(map(int, input().split()))
        for j in range(1, k):
            f, t = a[j - 1] - 1, a[j] - 1
            if a[j - 1] == a[j]:
                print("No")
                return

            g[f].append(t)
            g_t[t].append(f)

    cnt, _ = scc(n, g, g_t)
    print("Yes" if cnt == n else "No")


main()