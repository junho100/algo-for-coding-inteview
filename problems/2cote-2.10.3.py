N, M = map(int, input().split())
parent = [0]*(N+1)

for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if (a < b):
        parent[b] = a
    else:
        parent[a] = b


edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort(key = lambda x : x[0])

result = 0
largest_edge = 0

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        largest_edge = max(largest_edge, c)

print(result - largest_edge)