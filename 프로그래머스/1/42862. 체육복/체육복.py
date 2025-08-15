def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    lo = lost.copy()
    
    for i in lost:
        if i in reserve:
            lo.remove(i)
            reserve.remove(i)
            continue
    lost = lo.copy()
    
    for i in lost:
        
        if i-1 in reserve:
            lo.remove(i)
            reserve.remove(i-1)
            continue
        if i+1 in reserve:
            lo.remove(i)
            reserve.remove(i+1)
            continue

    
    
    
    return n-len(lo)