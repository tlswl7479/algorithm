from collections import deque
queue = deque()

n = int(input())

for i in range(1, n+1):
  queue.append(i)

while queue:
  if len(queue) == 1:
    print(*queue)
    break
  else:
    queue.popleft()
    queue.append(queue.popleft())
