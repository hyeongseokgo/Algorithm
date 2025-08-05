def solution(n, m, section):
    answer = 0
    section.sort()
    paint = 0
    for i in range(len(section)):
        temp = section[i]
        if temp > paint:
            
            answer += 1
            paint = (temp+m)-1
        
    
    
    return answer