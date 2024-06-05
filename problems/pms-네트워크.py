def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    answer = 0
    
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if find_parent(parent, i) != find_parent(parent, j):
                    union(parent, i, j)
                    
    for i in range(n):
        find_parent(parent, i)
    
    parent_set = set(parent)
    
    answer = len(parent_set)
    
    return answer