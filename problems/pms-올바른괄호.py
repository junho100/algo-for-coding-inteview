def check_correct(a, b):
    if a == "(" and b == ")":
        return True
    
    return False

def solution(s):
    answer = True
    
    arr = []
    
    for element in s:
        if len(arr) == 0:
            arr.append(element)
            continue
        
        target = arr.pop()
        
        if check_correct(target, element):
            continue
        else:
            arr.append(target)
            arr.append(element)
        
    if len(arr) != 0:
        return False
    else:
        return True