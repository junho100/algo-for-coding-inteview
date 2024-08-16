from itertools import product
import copy

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
candidates = list(product([i for i in range(4)], repeat=5))

result = 2

def move_element(g, x, y, d, visited):
    isMoved = True
    while isMoved:
        isMoved = False

        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or (g[nx][ny] != 0 and g[nx][ny] != g[x][y]):
            break

        if g[nx][ny] == g[x][y] and not visited[nx][ny]:
            g[nx][ny] *= 2
            g[x][y] = 0
            visited[nx][ny] = True
            visited[x][y] = False
        elif g[nx][ny] == 0:
            g[nx][ny] = g[x][y]
            g[x][y] = 0
            isMoved = True
        x = nx
        y = ny
        

def move_graph(g, d):
    isMerged = [[False]*N for _ in range(N)]
    if d == 0:
        for i in range(N):
            for j in range(N):
                if g[i][j] != 0:
                    move_element(g, i, j, d, isMerged)
    elif d == 1:
        for i in range(N-1, -1, -1):
            for j in range(N):
                if g[i][j] != 0:
                    move_element(g, i, j, d, isMerged)
    elif d == 2:
        for i in range(N):
            for j in range(N):
                if g[j][i] != 0:
                    move_element(g, j, i, d, isMerged)
    else:
        for i in range(N-1, -1, -1):
            for j in range(N):
                if g[j][i] != 0:
                    move_element(g, j, i, d, isMerged)

for candidate in candidates:
    copied_graph = copy.deepcopy(graph)
    for dir in candidate:
        move_graph(copied_graph, dir)
    
    result = max(result, max(list(map(max, copied_graph))))

print(result)