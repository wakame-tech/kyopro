class Tree:
  def __init__(self, n):
    self.edges = []
    self.adj = [[] for _  in range(n)]
    self.depth = [-1 for _ in range(n)]

  def add_edge(self, a, b):
    self.edges.append((a, b))
    self.adj[a].append(b)
    self.adj[b].append(a)

  def is_parent(self, a, b):
    return self.depth[a] < self.depth[b]

  def calc_depth(self):
    self.depth[0] = 0
    que = [0]
    while len(que) != 0:
      c = que.pop()
      # depth
      for v in self.adj[c]:
        if self.depth[v] == -1:
          self.depth[v] = self.depth[c] + 1
          que.append(v)

n = int(input())
tree = Tree(n)

for i in range(n - 1):
  a, b = map(int, input().split(' '))
  tree.add_edge(a - 1, b - 1)

tree.calc_depth()

diff = [0 for _ in range(n)]
q = int(input())

for i in range(q):
  t, e, x = map(int, input().split(' '))
  a, b = tree.edges[e - 1]

  # aが親, bが子
  if not tree.is_parent(a, b):
    a, b = b, a
    t = 2 if t == 1 else 1 # 矢印逆

  if t == 1:
    diff[0] += x
    # b より下は打ち消し
    diff[b] -= x
  else:
    diff[b] += x
  
# 子に累積和
que = [0]
while len(que) != 0:
  c = que.pop()
  for a in tree.adj[c]:
    if tree.is_parent(c, a):
      diff[a] += diff[c]
      que.append(a)

for d in diff:
  print(d)