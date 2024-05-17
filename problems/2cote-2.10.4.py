from collections import deque
import copy

N = int(input())
indegree = [0]*(N+1)
lecture_times = [0]
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    lecture_times.append(arr[0])
    for j in arr[1:]:
        if j == -1:
            break
        
        indegree[i] += 1
        graph[j].append(i)

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

dp = copy.deepcopy(lecture_times)

while queue:
    now = queue.popleft()

    for next in graph[now]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[now] + lecture_times[next])
        if (indegree[next] == 0):
            queue.append(next)

for i in range(1, N+1):
    print(dp[i])