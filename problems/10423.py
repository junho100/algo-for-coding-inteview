import heapq

N, M, K = map(int, input().split())
electrics = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
queue = []
for _ in range(M):
    u, v, w = map(int, input().split())

    heapq.heappush(queue, (w, u, v))
    
parent = [i for i in range(N+1)]
is_connected = [False]*(N+1)

for e in electrics:
    is_connected[e] = True

result = 0

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    
    return parent[x]

def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

def check_valid(parent):
    for i in range(1, N+1):
        if find_parent(i, parent) not in electrics:
            return False
    
    return True

while queue:
    cost, a, b = heapq.heappop(queue)

    a_parent = find_parent(a, parent)
    b_parent = find_parent(b, parent)

    if (a_parent != b_parent) and (is_connected[a_parent], is_connected[b_parent]).count(True) != 2:
        union(a, b, parent)
        result += cost
        if (is_connected[a_parent], is_connected[b_parent]).count(True) == 1:
            is_connected[a_parent] = True
            is_connected[b_parent] = True
print(result)

    
