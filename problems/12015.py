from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]

for a in arr:
    if result[-1] < a:
        result.append(a)
    else:
        idx = bisect_left(result, a)
        result[idx] = a

print(len(result))