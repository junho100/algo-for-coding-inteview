def solution(skill, skill_trees):
    skill_arr = list(skill)[::-1]
    answer = 0
    
    for skill_tree in skill_trees:
        indegree = [0]*(27)
        graph = [[] for _ in range(27)]
        
        for i in range(len(skill) - 1):
            indegree[ord(skill[i+1]) - ord('A')] += 1
            graph[ord(skill[i]) - ord('A')].append(ord(skill[i+1]) - ord('A'))
        
        for s in skill_tree:
            if (indegree[ord(s) - ord('A')] == 0):
                for next in graph[ord(s) - ord('A')]:
                    indegree[next] -= 1
            else:
                break
        else:
            answer += 1

    return answer