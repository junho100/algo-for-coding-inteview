N, M = map(int, input().split())
A, B, d = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

while True:
    arr[A][B] = 1
    result += 1

    for i in range(1, 5, 1):
        nx = A + dx[(d+i)%4]
        ny = B + dy[(d+i)%4]

        if (nx < 0 or ny < 0 or nx > N or ny > M or arr[nx][ny] == 1):
            continue
        A = nx
        B = ny
        d = (d+i)%4
        break
    else:
        nx = A - dx[(d+1)%4]
        ny = B - dy[(d+1)%4]
        if (arr[nx][ny] == 1):
            print(result)
            break
        A = nx
        B = ny