N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, list(input()))))

visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx < 0 or ny < 0 or nx >= N or ny >= N):
            continue

        if (not visited[nx][ny]) and (arr[nx][ny] == 1):
            cnt += dfs(nx, ny)

    return cnt


result = []

for i in range(N):
    for j in range(N):
        if (arr[i][j] == 1) and (not visited[i][j]):
            result.append(dfs(i, j))

print(len(result))
result.sort()
for r in result:
    print(r)