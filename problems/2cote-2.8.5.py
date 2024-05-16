N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [1e9]*10001

for a in arr:
    dp[a] = 1

for i in range(1, 10001):
    for a in arr:
        if (i-a)>0:
            dp[i] = min(dp[i], dp[i-a]+1)

if (dp[M] < 1e9):
    print(dp[M])
else:
    print(-1)