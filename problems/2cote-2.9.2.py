N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][K] + graph[K][X]
if (distance >= INF):
    print(-1)
else:
    print(distance)