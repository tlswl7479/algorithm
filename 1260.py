from collections import deque


def dfs(node):
  visit_dfs[node] = True
  dfs_list[node].sort()
  print(node, end=' ')
  for i in dfs_list[node]:
    if not visit_dfs[i]:
      dfs_r.append(i)
      dfs(i)

def bfs(node):
  visit_bfs[node] = True
  queue.append(node)
  while queue:
    node = queue.popleft()
    print(node, end=' ')
    for i in dfs_list[node]:
      if not visit_bfs[i]:
        visit_bfs[i] = True
        queue.append(i)
   


n, m, v = map(int, input().split())
visit_dfs = [False] * (n + 1)
visit_bfs = [False] * (n + 1)
dfs_list = [[] for _ in range(n + 1)]
dfs_r = []
queue = deque()

for i in range(m):
  a, b = map(int, input().split())
  dfs_list[a].append(b)
  dfs_list[b].append(a)

dfs_r.append(v)
dfs(v)
print()
bfs(v)
