def convert_to_int(date_str):
    date_int_arr = list(map(int, date_str.split('.')))
    date_int = date_int_arr[0]*(28*12) + date_int_arr[1]*28 + date_int_arr[2]
    
    return date_int

def solution(today, terms, privacies):
    answer = []
    today_int = convert_to_int(today)
    term_plus = dict()
    for term in terms:
        name, month = term.split()
        term_plus[name] = int(month)*28
    
    for i in range(len(privacies)):
        priv = privacies[i]
        now, category = priv.split()
        now_int = convert_to_int(now)
        now_int += term_plus[category]
        now_int -= 1
        
        if now_int < today_int:
            answer.append(i+1)
    
    answer.sort()
    
    return answer