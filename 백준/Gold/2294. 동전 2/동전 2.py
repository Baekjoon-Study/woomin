n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
for c in range(len(coin)):
    for i in range(coin[c],k+1):
        if i - coin[c] != 0 and dp[i-coin[c]] == 0:
            continue        
        if dp[i] == 0:
            dp[i] = dp[i-coin[c]] + 1
        else:
            dp[i] = min(dp[i-coin[c]] + 1, dp[i])
if dp[k] == 0:
    print(-1)
else:
    print(dp[k])