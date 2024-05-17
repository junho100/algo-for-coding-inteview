import heapq

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
INF = int(1e9)
distance = [INF]*(N+1)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if (distance[now] < dist):
            continue

        for i in graph[now]:
            cost = distance[now] + i[0]

            if (cost < distance[i[1]]):
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

dijkstra(C)

cnt = 0
total = 0
for i in range(1, N+1):
    if ((distance[i] < INF) and i != C):
        cnt += 1
        total = max(total, distance[i])

print(cnt, total)