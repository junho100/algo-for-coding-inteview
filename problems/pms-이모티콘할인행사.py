from itertools import product

def solution(users, emoticons):
    answer = [-1, -1]
    # 10 20 30 40
    cans = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    
    for can in cans:
        register_cnt = 0
        emo_cnt = 0
        for user in users:
            total_price = 0
            for i in range(len(emoticons)):
                if can[i] >= user[0]:
                    total_price += (emoticons[i] * (100-can[i]) // 100)
            if total_price >= user[1]:
                register_cnt += 1
            else:
                emo_cnt += total_price
        answer = max(answer, [register_cnt, emo_cnt], key = lambda x : (x[0], x[1]))
    return answer