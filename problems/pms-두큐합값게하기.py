from collections import deque
    

def solution(queue1, queue2):
    answer = 0
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    for _ in range(len(queue1)*3):
        if sum1 == sum2:
            break
            
        if sum1 > sum2:
            tmp = queue1.popleft()
            sum1 -= tmp
            queue2.append(tmp)
            sum2 += tmp
        else:
            tmp = queue2.popleft()
            sum2 -= tmp
            queue1.append(tmp)
            sum1 += tmp
        answer += 1
        
    else:
        answer = -1
            
    return answer