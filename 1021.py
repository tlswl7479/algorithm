from collections import deque

queue = deque()

n, m = map(int, input().split())

for i in range(1, n + 1):
    queue.append(i)

# 뽑아내려고 하는 수의 위치 리스트를 입력 받음
lst = list(map(int, input().split()))

count = 0

for i in lst:
    index = queue.index(i)
    count += min(index, len(queue) - index)
    queue.rotate(-index)
    queue.popleft()

print(count)