import heapq

n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, d = map(int, input().split())

    graph[a].append((b, d))
    graph[b].append((a, d))


def dijkstra(start, distance):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



result = 0
INF = int(1e9)
for i in range(1, n+1):
    distance = [INF] * (n+1)

    dijkstra(i, distance)

    cnt = 0
    for j in range(1, n+1):
        if distance[j] <= m:
            cnt += items[j]
    
    result = max(cnt, result)

print(result)