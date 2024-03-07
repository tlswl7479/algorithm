import sys
sys.setrecursionlimit(10**6)

def dfs(r, c):
    check[r][c] = 1

    for i in range(4):
        nx = c + dx[i]
        ny = r + dy[i]
        if 0 <= nx < m and 0 <= ny < n and lst[ny][nx] == 1 and not check[ny][nx]:
            dfs(ny, nx)

t = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(t):
    m, n, k = map(int, input().split())
    lst = [[0 for _ in range(m)] for _ in range(n)] 
    check = [[0 for _ in range(m)] for _ in range(n)] 

    for _ in range(k):
        i, j = map(int, input().split())
        lst[j][i] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1 and not check[i][j]:
                dfs(i, j)
                count += 1

    print(count)
