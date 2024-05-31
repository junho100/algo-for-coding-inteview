from collections import deque
from math import ceil

def calculate(from_time, after_time):
    from_time = from_time.split(":")
    after_time = after_time.split(":")
    
    hour_dff = int(after_time[0]) - int(from_time[0])
    min_dff = int(after_time[1]) - int(from_time[1])
    
    return (hour_dff*60) + min_dff

def make_last_cost(total_time, dt, dc, st, ppt):
    if (total_time < dt):
        return dc
    
    result = dc + (ceil((total_time - dt) / st))*ppt
    
    return result

def solution(fees, records):
    answer = []
    default_time = fees[0]
    default_cost = fees[1]
    standard_time = fees[2]
    price_per_time = fees[3]
    
    queues = []
    queue_car_mapping = []
    
    total_times = {}
    
    for record in records:
        time_ex, car_num, op = record.split()
        
        if op == "IN":
            if car_num in queue_car_mapping:
                idx = queue_car_mapping.index(car_num)
                queues[idx].append(time_ex)
                continue
            else:
                total_times[car_num] = 0
                queues.append(deque([time_ex]))
                queue_car_mapping.append(car_num)
                continue
        else:
            idx = queue_car_mapping.index(car_num)
            in_time = queues[idx].popleft()
            
            between_time = calculate(in_time, time_ex)
            total_times[car_num] += between_time
            
    for i in range(len(queues)):
        if len(queues[i]) != 0:
            last = queues[i].popleft()
            between_time = calculate(last, "23:59")
            car_num = queue_car_mapping[i]
            total_times[car_num] += between_time
    result = []
    for k in total_times.keys():
        c = make_last_cost(total_times[k], default_time, default_cost, standard_time, price_per_time)
        result.append((k, c))
    
    result.sort(key = lambda x : int(x[0]))
    
    for r in result:
        answer.append(r[1])
            
    return answer