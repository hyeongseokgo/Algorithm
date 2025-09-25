def solution(routes):
    answer = 0
    
    routes.sort()
    
    start = -30001
    end = -30001
    
    for s, e in routes:
        if end < s:
            answer += 1
            start = s
            end = e
        else:
            if end > e:
                start = s
                end = e
            else:
                start = s
    
    return answer