from itertools import product
import copy
import sys

directions = [0, 1, 2, 3]

candidates = list(product(directions, repeat=10))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
graph = []
red_start_pos = ()
blue_start_pos = ()
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))
    for j in range(M):
        if graph[i][j] == "B":
            blue_start_pos = (i, j)
            continue
        if graph[i][j] == "R":
            red_start_pos = (i, j)
            continue

#return graph, red_pos, blue_pos -> when sink, (0,0)
def move_balls(graph, red_pos, blue_pos, dir):

    isOk = True
    while isOk:
        isOk = False
        nx_red = red_pos[0] + dx[dir]
        ny_red = red_pos[1] + dy[dir]
        nx_blue = blue_pos[0] + dx[dir]
        ny_blue = blue_pos[1] + dy[dir]

        if graph[nx_red][ny_red] == "O":
            graph[red_pos[0]][red_pos[1]] = "."
            red_pos = (0,0)
        
        if graph[nx_blue][ny_blue] == "O":
            graph[blue_pos[0]][blue_pos[1]] = "."
            blue_pos = (0,0)

        if graph[nx_red][ny_red] not in ["#", "B", "R"] and red_pos != (0,0):
            graph[red_pos[0]][red_pos[1]] = "."
            graph[nx_red][ny_red] = "R"
            red_pos = (nx_red, ny_red)
            isOk = True
        
        if graph[nx_blue][ny_blue] not in ["#", "B", "R"] and blue_pos != (0,0):
            graph[blue_pos[0]][blue_pos[1]] = "."
            graph[nx_blue][ny_blue] = "B"
            blue_pos = (nx_blue, ny_blue)
            isOk = True
        
    return graph, red_pos, blue_pos

# return true or false
def check_graph(red_pos, blue_pos):
    if red_pos == (0,0) and blue_pos != (0, 0):
        return True
    else:
        return False

result = int(1e9)

for can in candidates:
    test_graph = copy.deepcopy(graph)
    red_pos = red_start_pos
    blue_pos = blue_start_pos
    cnt = 0
    prev_dir = -1
    for d in can:
        if prev_dir == d:
            break

        if prev_dir == 0 and d == 1:
            break

        if prev_dir == 1 and d == 0:
            break

        if prev_dir == 2 and d == 3:
            break

        if prev_dir == 3 and d == 2:
            break

        test_graph, red_pos, blue_pos = move_balls(test_graph, red_pos, blue_pos, d)

        cnt += 1
        prev_dir = d

        if result < cnt:
            break
            
        if blue_pos == (0,0):
            break

        if check_graph(red_pos, blue_pos):
            result = min(result, cnt)
            break

if result == int(1e9):
    print(-1)
else:
    print(result)