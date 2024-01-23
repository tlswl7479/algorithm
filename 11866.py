from collections import deque
n, k = map(int, input().split())
lst = []
queue = deque()
count = k - 1

for i in range(n):
  queue.append(i + 1)

while queue:
  for i in range(k-1):
    queue.append(queue.popleft())
  lst.append(queue.popleft())

print("<", end='')
print(', '.join(map(str, lst)), end='')
print(">")