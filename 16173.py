def dfs(r, c):
    n = lst[r][c]
    chk[r][c] = 1

    if r == N - 1 and c == N - 1:  
        print("HaruHaru")
        exit()  

    if (r + n) < N and not chk[r + n][c]:  
        dfs(r + n, c)
    if (c + n) < N and not chk[r][c + n]:  
        dfs(r, c + n)

N = int(input())
lst = []
chk = [[0] * N for _ in range(N)]

for i in range(N):
    lst.append(list(map(int, input().split())))

dfs(0, 0)
print("Hing")  
