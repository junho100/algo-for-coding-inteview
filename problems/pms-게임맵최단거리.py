from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    answer = -1
    
    N = len(maps)
    M = len(maps[0])
    
    visited = [[0]*M for _ in range(N)]
    
    x = 0
    y = 0
    queue = deque([])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
            
        if maps[nx][ny] == 0:
            continue
            
        if nx == N-1 and ny == M-1:
            return 2
        
        visited[nx][ny] = 2
        queue.append((nx, ny))
    
    while queue:
        now = queue.popleft()
        
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if maps[nx][ny] == 0:
                continue
            
            if visited[nx][ny] == 0:
                if nx == N-1 and ny == M-1:
                    return visited[now[0]][now[1]] + 1
                visited[nx][ny] = visited[now[0]][now[1]] + 1
                queue.append((nx, ny))
            
    return answer