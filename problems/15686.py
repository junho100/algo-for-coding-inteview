from itertools import combinations

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append([i, j])
        if graph[i][j] == 1:
            houses.append([i, j])  
result = int(1e9)
for i in range(1, M+1):
    candidates = list(combinations(chickens, i))

    for candidate in candidates:
        dis = 0
        for house in houses:
            temp = int(1e9)
            for c in candidate:
                temp = min(temp, abs(house[0] - c[0]) + abs(house[1] - c[1]))
            
            dis += temp
        
        result = min(result, dis)

print(result)

# chickens = []
# houses = []
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 2:
#             chickens.append([i, j])
#         if graph[i][j] == 1:
#             houses.append([i, j])

# result = int(1e9)

# survived = []

# def cal(sur, ho):
#     r = 0
#     for a, b in ho:
#         min_dis = int(1e9)
#         for x, y in sur:
#             min_dis = min(min_dis, abs(a-x) + abs(b-y))
#         r += min_dis
#     return r

# def dfs(cnt):
#     global result
#     if cnt <= M:
#         result = min(result, cal(survived, houses))
#     else:
#         return
    
#     for c in chickens:
#         if c not in survived:
#             survived.append(c)
#             dfs(cnt+1)
#             survived.pop()

# for c in chickens:
#     survived.append(c)
#     dfs(1)
#     survived.pop()
# print(result)