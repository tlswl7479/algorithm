from collections import deque

def min_operations_to_k(A, K):
    visited = [False] * (K + 1)
    queue = deque([(A, 0)])  # (현재 값, 연산 횟수)를 저장하는 큐

    while queue:
        current, operations = queue.popleft()
        if current == K:
            return operations

        # 1을 더함
        next_value = current + 1
        if next_value <= K and not visited[next_value]:
            visited[next_value] = True
            queue.append((next_value, operations + 1))

        # 2를 곱함
        next_value = current * 2
        if next_value <= K and not visited[next_value]:
            visited[next_value] = True
            queue.append((next_value, operations + 1))

    return -1  # 도달할 수 없는 경우

A, K = map(int, input().split())

result = min_operations_to_k(A, K)
print(result)
