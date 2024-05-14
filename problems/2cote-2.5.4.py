from collections import deque

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, list(input()))))

visited = [[False]*M for _ in range(N)]

# 0,0 -> N-1, M-1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([[0,0]])
while queue:
    x, y = queue.popleft()
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx < 0 or ny < 0 or nx >= N or ny >= M or arr[nx][ny] == 0 or visited[nx][ny] == True):
            continue

        arr[nx][ny] = arr[x][y] + 1
        queue.append([nx, ny])

print(arr[N-1][M-1])