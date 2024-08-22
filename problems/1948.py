from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range((n+1))]
indegree = [0]*(n+1)

for _ in range(m):
    a, b, cost = map(int,sys.stdin.readline().split())

    graph[a].append((b, cost))
    indegree[b] += 1

start, end = map(int,sys.stdin.readline().split())

local_time = [0]*(n+1)
local_max_route = [set()] * (n+1)

def start_visit(s, e):
    queue = deque([s])

    while queue:
        start = queue.popleft()

        if start == e:
            print(local_time[start])
            print(len(local_max_route[start]))
            exit()
        
        for next in graph[start]:
            indegree[next[0]] -= 1

            if local_time[next[0]] < (local_time[start] + next[1]):
                local_time[next[0]] = (local_time[start] + next[1])
                local_max_route[next[0]] = local_max_route[start] | set([str([start, next[0]])])
            elif local_time[next[0]] == (local_time[start] + next[1]):
                local_max_route[next[0]] = local_max_route[next[0]] | local_max_route[start]
                local_max_route[next[0]].add(str([start, next[0]]))

            if indegree[next[0]] == 0:
                queue.append(next[0])

start_visit(start, end)