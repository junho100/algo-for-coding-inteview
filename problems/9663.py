N = int(input())
graph = [[0]*N for _ in range(N)]

queens = []
cnt = 0

def check(x, y):
    for queen in queens:
        if queen[1] == y or (abs(queen[0] - x) == abs(queen[1] - y)):
            return False
    
    return True

def dfs(depth):
    global cnt

    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        if check(depth, i):
            queens.append([depth, i])
            dfs(depth+1)
            queens.pop()

for i in range(N):
    queens.append([0, i])
    dfs(1)
    queens.pop()

print(cnt)
