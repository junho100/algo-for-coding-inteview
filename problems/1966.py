from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_with_mark = []
    for i in range(N):
        if (i == M):
            arr_with_mark.append((arr[i], True))
        else:
            arr_with_mark.append((arr[i], False))

    queue = deque(arr_with_mark)
    result = 0
    while queue:
        now = queue.popleft()
        if (len(queue) == 0 or now[0] >= max(queue, key = lambda x : x[0])[0]):
            result += 1
            if now[1]:
                print(result)
                break
        else:
            queue.append(now)
            continue