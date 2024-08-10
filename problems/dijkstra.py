import heapq

n = int(input())

INF = int(1e9)
distance = [INF] * n

graph = [[] for _ in range(n)]

def dijkstra(start):
    q = []

    heapq.heappush((0, start))
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