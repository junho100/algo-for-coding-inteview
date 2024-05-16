# first -> 0
# dp[x] = dp[x-2] + arr[x]

# first -> x
# dp[x] = dp[x-1]

N = int(input())
arr = [-1] + list(map(int,input().split()))

dp = [0]*101
dp[1] = arr[1]
dp[2] = max(arr[1], arr[2])

for i in range(3, N+1):
    dp[i] = max(dp[i-2]+arr[i], dp[i-1])
print(dp[N])