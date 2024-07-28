from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([i for i in range(len(priorities))])
    
    while len(queue) != 0:
        element = queue.popleft()
        if priorities[element] >= max(priorities):
            priorities[element] = 0
            answer += 1
            
            if location == element:
                break
            continue
        else:
            queue.append(element)
    return answer