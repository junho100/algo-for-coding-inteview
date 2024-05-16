N, M = map(int, input().split())
cakes = list(map(int, input().split()))

start = 0
end = max(cakes)
result = 0
cakes.sort()

def slice_cake(target, arr):
    m = 0
    for a in arr:
        if (a > target):
            m += (a - target)
    
    return m

while start <= end:
    mid = (start + end) // 2

    if (slice_cake(mid, cakes) == M):
        print(mid)
        exit()

    if (slice_cake(mid, cakes) < M):
        end = mid - 1

    if (slice_cake(mid, cakes) > M):
        start = mid + 1
        result = max(result, mid)

print(result)