def solution(record):
    answer = []
    chat = {}
    log = []
    
    for r in record:
        arr = r.split()
        op = arr[0]
        
        # 0 -> enter
        # 1 -> leave
        
        if (op == 'Enter'):
            identify = arr[1]
            name = arr[2]
            log.append((0, identify))
            chat[identify] = name
        
        if (op == 'Change'):
            identify = arr[1]
            name = arr[2]
            chat[identify] = name
        
        if (op == 'Leave'):
            identify = arr[1]
            log.append((1, identify))
    
    for l in log:
        if l[0] == 0:
            answer.append(chat[l[1]]+"님이 들어왔습니다.")
        if l[0] == 1:
            answer.append(chat[l[1]]+"님이 나갔습니다.")

    return answer