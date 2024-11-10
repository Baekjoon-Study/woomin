#12865
n, k = map(int,input().split())
obj = [list(map(int,input().split())) for _ in range(n)] # w,v
obj.insert(0,[0,0])
dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(1,k+1):
    for j in range(1,n+1):
        if i < obj[j][0]:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-obj[j][0]][j-1] + obj[j][1])
print(dp[k][n])