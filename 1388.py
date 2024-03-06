import sys

n, m = map(int, sys.stdin.readline().split())  # 세로 n 가로 m
place = []
for _ in range(n):
    place.append(list(sys.stdin.readline()))

def dfs(row, col):
    if place[row][col] == "-":
        place[row][col] = 1  # 방문처리
        for a in [1, -1]:  # 같은행 확인하기 양옆
            Y = col + a  # 같은 나무판자로 만들기
            if (0 < Y < m) and place[row][Y] == "-":  # 가로를 벗어나지않고 다음 노드가 - 라면 다시 재귀
                dfs(row, Y)
    if place[row][col] == "|":
        place[row][col] = 1
        for b in [1, -1]:  # 같은열 확인하기 위아래
            X = row + b
            if (0 < X < n) and place[X][col] == "|":  # 세로를 벗어나지않고 다음 노드가 | 라면 다시 재귀
                dfs(X, col)


count = 0
for i in range(n):  # 세로 길이만큼
    for j in range(m):  # 가로 길이만큼
        if place[i][j] == '-' or place[i][j] == "|":  # 다음노드가 - 나 |일 경우
            dfs(i, j)  # 재귀함수 호출
            count += 1

print(count)