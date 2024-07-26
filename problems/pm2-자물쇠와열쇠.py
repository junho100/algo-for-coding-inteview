import copy

def padding_lock(prev_lock, size):
    after_lock = []
    
    for _ in range(size):
        after_lock.append([1]*(len(prev_lock) + 2*size))
    
    for i in range(len(prev_lock)):
        padded_row = [1]*size + prev_lock[i] + [1]*size
        after_lock.append(padded_row)
        
    for _ in range(size):
        after_lock.append([1]*(len(prev_lock) + 2*size))
    
    return after_lock

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def input_key(padded_lock, key, x, y):
    result = copy.deepcopy(padded_lock)
    
    for i in range(len(key)):
        for j in range(len(key)):
            result[x+i][y+j] += key[i][j]
    
    return result

def check_lock(target_key, lock_size, key_size):
    dump = [[0]*len(target_key) for _ in range(len(target_key))]
    for i in range(lock_size):
        for j in range(lock_size):
            dump[i+key_size][j+key_size] = 1
            if target_key[i+key_size][j+key_size] != 1:
                return False
    return True

def solution(key, lock):
    padded_lock = padding_lock(lock, len(key))
    
    M = len(key)
    N = len(lock)
    
    for i in range(len(padded_lock) - M + 1):
        for j in range(len(padded_lock) - M + 1):
            for _ in range(4):
                after_input_key = input_key(padded_lock, key, i, j)
                
                if check_lock(after_input_key, N, M):
                    return True
                
                key = rotate_90(key)
    
    return False