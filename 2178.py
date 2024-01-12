from collections import deque

def bfs(x, y):
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == '1':
                array[nx][ny] = str(int(array[x][y]) + 1)  # '1'을 거리 문자열로 업데이트
                queue.append([nx, ny])
    return int(array[n - 1][m - 1])  # 최종 결과를 다시 int로 변환

n, m = map(int, input().split())
array = []
queue = deque()

# 움직일 수 있는 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]  

for i in range(n):
    row = input()
    array.append(list(row))  # 각 행을 리스트로 추가

print(bfs(0, 0))
