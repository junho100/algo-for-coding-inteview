N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, list(input()))))

def dfs(graph, x, y):
    if (x < 0 or y < 0 or x >= N or y >= M):
        return
    
    if (graph[x][y] == 0):
        graph[x][y] = 1
        dfs(graph, x-1, y)
        dfs(graph, x+1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)

result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            dfs(arr, i, j)
            result += 1

print(result)