def solution(n, words):
    answer = []

    my_turn = [0]*(n+1)
    start = 1
    used_words = []
    
    for word in words:
        my_turn[start] += 1
        
        if len(used_words) == 0:
            used_words.append(word)
            start = (start + 1)%(n+1)
            if (start == 0):
                start = 1
            continue
        
        if (used_words[-1][-1] != word[0]):
            answer.append([start, my_turn[start]])
            break
        
        if (word in used_words):
            answer.append([start, my_turn[start]])
            break
        
        if (len(word) == 1):
            answer.append([start, my_turn[start]])
            break
            
        used_words.append(word)
        start = (start + 1)%(n+1)
        if (start == 0):
            start = 1
    else:
        answer.append([0, 0])

    return answer[0]