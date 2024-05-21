from itertools import permutations
import sys

input = sys.stdin.readline
N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

exp = list(map(int, input().rstrip().split()))
tmp = []
for i in range(4):
    for j in range(exp[i]):
        tmp.append(i)

cans = list(permutations(tmp))
M = -10**10
m = 10**10
for can in cans:
    result = nums[0]

    for i in range(1, N):
        if can[i-1] == 0:
            result += nums[i]
        elif can[i-1] == 1:
            result -= nums[i]
        elif can[i-1] == 2:
            result *= nums[i]
        else:
            if result < 0:
                result *=(-1)
                result = result//nums[i]
                result *=(-1)
            else:
                result = result // nums[i]
    M = max(M, result)
    m = min(m, result)

print(M)
print(m)