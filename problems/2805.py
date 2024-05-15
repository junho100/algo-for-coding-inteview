N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

def get_tree(cut_length):
    r = 0
    for a in arr:
        if (cut_length < a):
            r += (a - cut_length)
    return r

while start <= end:
    mid = (start + end) // 2

    if (get_tree(mid) == M):
        result = mid
        break

    if (get_tree(mid) > M):
        start = mid+1
        result = max(result, mid)
    
    if (get_tree(mid) < M):
        end = mid-1
print(result)