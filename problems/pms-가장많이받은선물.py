from itertools import combinations

def get_gift_value(t, idx):
    tmp = 0
    for i in range(len(t)):
        tmp += t[i][idx]
    return sum(t[idx]) - tmp

def solution(friends, gifts):
    answer = 0
    gift_table = [[0]*(len(friends)) for _ in range(len(friends))]
    pred_gift = [0]*(len(friends))
    
    for gift in gifts:
        a, b = gift.split()
        a_idx = friends.index(a)
        b_idx = friends.index(b)
        
        gift_table[a_idx][b_idx] += 1
    
    cans = list(combinations([i for i in range(len(friends))], 2))
    
    for can in cans:
        i, j = can
        if gift_table[i][j] > gift_table[j][i]:
            pred_gift[i] += 1
        elif gift_table[i][j] < gift_table[j][i]:
            pred_gift[j] += 1
        else:
            if get_gift_value(gift_table, i) > get_gift_value(gift_table, j):
                pred_gift[i] += 1
            elif get_gift_value(gift_table, i) < get_gift_value(gift_table, j):
                pred_gift[j] += 1

                
    return max(pred_gift)