N = int(input())
actions = list(input().split())

arr = []
for _ in range(N+1):
    arr.append([0 for _ in range(N+1)])

x = 1
y = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
action = ["U", "D", "L", "R"]

for i in range(len(actions)):
    for j in range(4):
        if (actions[i] == action[j]):
            temp_x = x + dx[j]
            temp_y = y + dy[j]

            if (temp_x > N or temp_x < 1 or temp_y > N or temp_y < 1):
                continue

            x = temp_x
            y = temp_y

print(x, y)
