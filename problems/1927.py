import heapq
import sys

queue = []

N = int(sys.stdin.readline())

for _ in range(N):
    op = int(sys.stdin.readline())

    if op == 0:
        if len(queue) == 0:
            print(0)
        else:
            print(heapq.heappop(queue))
    else:
        heapq.heappush(queue, op)