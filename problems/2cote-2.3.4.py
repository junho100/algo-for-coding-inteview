N, K = map(int, input().split())
result = 0
while True:
    if (N == 1):
        print(result)
        break
    if (N % K == 0):
        N /= K
        result += 1
        continue

    N -= 1
    result += 1