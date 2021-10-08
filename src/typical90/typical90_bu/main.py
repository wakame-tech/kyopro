
order = []

def dfs(tree, children, flags, p):
    flags[p] = True
    for i in tree[p]:
        if not flags[i]:
            children[p].append(i)
            dfs(tree, children, flags, i)
    order.append(p)

from functools import reduce


def prodmod(a, md):
    return reduce(lambda x, y: x * y % md, a) % md

if __name__ == "__main__":
    n = int(input())
    md = 10 ** 9 + 7
    dp  = [[0 for x in range(3)] for y in range(n)]
    c = list(map(str, input().split()))
    tree = [[] for _ in range(n)]
    children = [[] for _ in range(n)]
    flags = [False] * (n + 1)
    for i in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    dfs(tree, children, flags, 0)
    # print(order)
    # print(tree)
    # print(children)

    for pos in order:
        if len(children[pos]) == 0:
            if c[pos] == 'a':
                dp[pos][0] = 1
            else:
                dp[pos][1] = 1
            # print(pos, c[pos], dp[pos])
            continue

        if c[pos] == 'a':
            dp[pos][0] = prodmod([dp[b][0] + dp[b][2] for b in children[pos]], md)
            dp[pos][2] = prodmod([dp[b][0] + dp[b][1] + 2 * dp[b][2] for b in children[pos]], md) - prodmod([dp[b][0] + dp[b][2] for b in children[pos]], md)
        else:
            dp[pos][1] = prodmod([dp[b][1] + dp[b][2] for b in children[pos]], md)
            dp[pos][2] = prodmod([(dp[b][0] + dp[b][1] + 2 * dp[b][2]) for b in children[pos]], md) - prodmod([dp[b][1] + dp[b][2] for b in children[pos]], md)
        # print(pos, c[pos], dp[pos])

    print(dp[0][2] % md)
