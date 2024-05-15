from collections import deque

N, M, V = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

for ele in arr:
    ele.sort()

def dfs(v):
    visited[v] = True
    print(v, end = " ")
    for ele in arr[v]:
        if not visited[ele]:
            dfs(ele)

def bfs(v):
    queue = deque()
    visited[v] = True
    queue.append(v)

    while queue:
        now = queue.popleft()
        print(now, end = " ")

        for ele in arr[now]:
            if not visited[ele]:
                queue.append(ele)
                visited[ele] = True

for z in range(2):
    visited = [False]*(N+1)
    if z == 0:
        dfs(V)
        print()
    else:
        bfs(V)
        print()