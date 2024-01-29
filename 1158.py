from collections import deque

n, k = map(int, input().split())
queue = deque()
lst = []

for i in range(1, n+1):
  queue.append(i)

while queue:
  queue.rotate(-k)
  lst.append(queue.pop())

print("<", end = "")
print(lst[0], end = "")
for i in range(1, len(lst)):
  print(", %d" %lst[i], end = "")
print(">")