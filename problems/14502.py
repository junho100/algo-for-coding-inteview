from itertools import combinations
from collections import deque

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

candidates = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            candidates.append((i, j))

comb = list(combinations(candidates, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        now = queue.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if (nx < 0 or ny < 0 or nx >= N or ny >= M):
                continue

            if (not visited[nx][ny]) and (not arr[nx][ny] == 1):
                queue.append((nx, ny))
                visited[nx][ny] = True

for c in comb:
    visited = [[False]*M for _ in range(N)]
    for position in c:
        arr[position[0]][position[1]] = 1
    
    for i in range(N):
        for j in range(M):
            if (not visited[i][j]) and arr[i][j] == 2:
                bfs(i, j)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and not visited[i][j]:
                cnt += 1
    
    result = max(cnt, result)

    for position in c:
        arr[position[0]][position[1]] = 0

print(result)