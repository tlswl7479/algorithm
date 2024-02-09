# 흰 도화지의 크기
canvas_size = 100

# 검은색 영역을 저장할 2차원 배열 초기화
black_area = [[0] * canvas_size for _ in range(canvas_size)]

# 색종이의 수 입력
num_papers = int(input())

# 색종이를 검은색 영역에 반영
for _ in range(num_papers):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            black_area[i][j] = 1

# 검은색 영역의 넓이 계산
total_area = sum(sum(row) for row in black_area)
print(total_area)
