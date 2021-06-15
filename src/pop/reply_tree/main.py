from icecream import ic
from anytree import Node

def branches(leaf: Node):
    """ leaf の分岐数 """
    cnt = 0
    for i, anc in enumerate(leaf.iter_path_reverse()):
        if anc.height != i:
            cnt += 1
    return cnt

def prune(leaf: Node):
    """ leaf の枝をかる """
    n = leaf
    while len(n.siblings) == 0:
        n = n.parent
    n.parent = None

def flatten(root: Node):
    """ 兄弟がいないならまとめる """
    cs = root.children
    if len(cs) == 0:
        return [root]
    elif len(cs) == 1:
        return [root, *flatten(cs[0])]
    else:
        res = []
        l0, *l1s = sorted(cs, key=lambda n: branches(n), reverse=True)
        l0s = flatten(l0)

        # [root, l0[0], l1..., l0[1:]]
        res.append(root)
        res.append(l0s[0])
        for l1 in l1s:
            res.append(flatten(l1))
        res.extend(l0s[1:])
        return res

def flatten_by_lt_l1(root: Node):
    """ level1 以下を枝刈りしてまとめる """
    for leaf in root.leaves:
        if branches(leaf) > 1:
            prune(leaf)
    return flatten(root)

def construct_tree(n: int, links: list):
    """ 隣接情報から木を構築 """
    nodes = [Node(i + 1) for i in range(n)]
    for i, p in links:
        nodes[i - 1].parent = nodes[p - 1]
    return nodes

if __name__ == '__main__':
    # 入力
    n = int(input())
    links = []
    for i in range(n - 1):
        i, p = map(int, input().split())
        links.append((i, p))

    # 計算
    nodes = construct_tree(n, links)
    res = flatten_by_lt_l1(nodes[0])

    # 出力
    for e in res:
        if type(e) is list:
            print(list(map(lambda n: n.name, e)), end=' ')
        else:
            print(e.name, end=' ')