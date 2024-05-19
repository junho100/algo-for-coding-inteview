def solution(s):
    answer = 1001
    
    for i in range(1, len(s)+1):
        arr = []
        count = []
        for j in range(0, len(s), i):
            if len(arr) == 0:
                arr.append(s[j:j+i])
                count.append(1)
                continue
            
            if (arr[-1] == s[j:j+i]):
                count[-1] += 1
                continue
            else:
                arr.append(s[j:j+i])
                count.append(1)
        total = ''
        for i in range(len(arr)):
            if (count[i] != 1):
                total += str(count[i])
            total += arr[i]
        answer = min(answer, len(total))
    return answer