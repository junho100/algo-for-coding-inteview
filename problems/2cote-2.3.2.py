n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
first = arr[0]
second = arr[1]
cnt = 0
result = 0
max_add = 0
while True:
    if cnt == m:
        print(result)
        break

    if (max_add == k):
        max_add = 0
        result += second
        cnt += 1
        continue
    result += first
    max_add += 1
    cnt += 1
    