n = int(input())
dp = list(map(int,input().split()))
dp.insert(0,0)
for i in range(1,n+1):
    for j in range(1,i):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[n])