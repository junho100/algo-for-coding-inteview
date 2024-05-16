N = int(input())
products = list(map(int, input().split()))
M = int(input())
needs = list(map(int, input().split()))
products.sort()

def bsearch(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if (arr[mid] == target):
            return True
        
        if (arr[mid] > target):
            end = mid - 1
        
        if (arr[mid] < target):
            start = mid + 1
    
    return False

for need in needs:
    if bsearch(products, need):
        print('yes', end = " ")
    else:
        print('no', end = " ")