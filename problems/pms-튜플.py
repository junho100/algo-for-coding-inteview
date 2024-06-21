def solution(s):
    answer = []
    
    arr = s[1:-1].split("},{")
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-1]
    arr.sort(key = lambda x : len(x))
    for a in arr:
        ele_arr = list(map(int, a.split(',')))
        for j in ele_arr:
            if j not in answer:
                answer.append(j)

    return answer