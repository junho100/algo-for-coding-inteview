N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

result_arr = []

for i in range(N):
    result_arr.append(min(arr[i]))

print(max(result_arr))