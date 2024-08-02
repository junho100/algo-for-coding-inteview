answer = int(1e9)

def solution(begin, target, words):
    global answer
    visited = [False]*len(words)
    
    for i in range(len(words)):
        if check_two_words(begin, words[i]):
            visited[i] = True
            dfs(visited, words, i, 1, target)
            visited[i] = False
    
    if answer == int(1e9):
        return 0
    else:
        return answer

def check_two_words(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    
    if cnt == len(a)-1:
        return True
    else:
        return False

def dfs(visited, words, now, cnt, target):
    global answer
    
    if words[now] == target:
        answer = min(answer, cnt)
    else:
        for i in range(len(words)):
            if not visited[i] and check_two_words(words[now], words[i]):
                visited[i] = True
                dfs(visited, words, i, cnt+1, target)
                visited[i] = False