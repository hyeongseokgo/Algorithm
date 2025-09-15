# 등굣길

def solution(m, n, puddles):
    answer = 0
    
    dp = [[-1]*m for _ in range(n)]
    
    for i in range(m):
        dp[0][i] = 1
    
    for i in range(n):
        dp[i][0] = 1
        
    for i in puddles:
        if i[1]-1 == 0:
            for x in range(i[0]-1, m):
                dp[0][x] = 0

        elif i[0]-1 == 0:
            for y in range(i[1]-1, n):
                dp[y][0] = 0

        else:
            dp[i[1]-1][i[0]-1] = 0
        
    for i in range(1, m):
        for j in range(1, n):
            if dp[j][i] == 0:
                continue
            else:
                dp[j][i] = (dp[j-1][i] + dp[j][i-1])%1000000007
                               
    
    return dp[n-1][m-1]