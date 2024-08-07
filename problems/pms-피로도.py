from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    candidates = list(permutations(dungeons))
    
    for can in candidates:
        life = k
        cnt = 0
        
        for d in can:
            if life < d[0]:
                break
            
            cnt += 1
            life -= d[1]
        
        answer = max(answer, cnt)
    return answer