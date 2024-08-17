import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
result = [-1]*N

def sol1(r):
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[j] > arr[i]:
                r[i] = arr[j]
                break

def sol2(r):
    stack = [0]

    for i in range(1, N):
        while stack and arr[stack[-1]] < arr[i]:
            r[stack.pop()] = arr[i]
        
        stack.append(i)

sol2(result)
    
print(" ".join(list(map(str, result))))