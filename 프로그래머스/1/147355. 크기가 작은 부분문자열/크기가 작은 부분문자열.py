def solution(t, p):
    
    length_p = len(p)
    length_t = len(t)
    time = 0
    for i in range(0, length_t-length_p+1):
        if int(t[i:i+length_p]) <= int(p):
            time += 1
    
    return time