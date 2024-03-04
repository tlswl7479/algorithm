def pascals_triangle_element(n, k):
    dp = [[0] * (i + 1) for i in range(n)]
    
    for i in range(n):
        dp[i][0] = dp[i][i] = 1
    
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    return dp[n - 1][k - 1]

n, k = map(int, input().split())

print(pascals_triangle_element(n, k))
