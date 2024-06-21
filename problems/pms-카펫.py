def check_carpet(cnt, graph):
    
    n = len(graph)
    m = len(graph[0])
    
    result = 2*(m+n) - 4
    if cnt != result:
        return False
    
    return True

def solution(brown, yellow):
    answer = []
    total  = brown + yellow
    
    M = total // 2
    
    for i in range(M, 0, -1):
        if total % i == 0:
            height = total // i
            carpet = [[0] * i for _ in range(height)]
            
            if check_carpet(brown, carpet):
                answer = [i, height]
                break
            
    return answer