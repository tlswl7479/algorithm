from collections import deque
import sys

def bfs(node):
  global count
  visit_list[node] = True
  queue.append(node)
  while queue:
    node = queue.popleft()
    for i in list[node]:
      if not visit_list[i]:
        visit_list[i] = True
        count += 1
        queue.append(i)
  print(count)
  count = 0

t = int(input())
queue = deque()
count = 0

for _ in range(t):
  n, m = map(int, sys.stdin.readline().split())
  list = [[] for _ in range(n + 1)]
  visit_list = [[] for _ in range(n + 1)]
  for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    list[b].append(a)
    list[a].append(b)
  bfs(1)

