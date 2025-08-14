def solution(s):
    answer = 0
    save = ''
    
    xtime = 0
    time = 0
    for i in range(len(s)):
        if len(save) == 0:
            save = s[i]
            xtime = 1
        else:
            if save == s[i]:
                xtime += 1
            else:
                time += 1
            
            if xtime == time:
                answer += 1
                save = ''
                xtime =0
                time =0
        
    if xtime != 0:
        answer += 1
        
    return answer