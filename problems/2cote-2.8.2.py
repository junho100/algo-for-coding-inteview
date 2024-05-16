INF = 1e9

dp = [INF]*30001
dp[1] = 0
dp[2] = 1
dp[4] = 2
dp[3] = 1
dp[5] = 1

for i in range(6, 30001):
    if (i%5 == 0):
        dp[i] = min(dp[i], dp[i//5]+1)
    if (i%3 == 0):
        dp[i] = min(dp[i], dp[i//3]+1)
    if (i%2 == 0):
        dp[i] = min(dp[i], dp[i//2]+1)
    dp[i] = min(dp[i], dp[i-1]+1)
X = int(input())
print(dp[X])