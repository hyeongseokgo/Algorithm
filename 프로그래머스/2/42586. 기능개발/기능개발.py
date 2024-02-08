import math

def solution(progresses, speeds):
    answer = []
    
    days = []
    for i in range(len(speeds)):
        a = math.ceil((100 - progresses[i])/speeds[i])
        days.append(a)
        
    cnt = 1
    for j in range(1, len(days)):
        if days[j-cnt] < days[j]:
            answer.append(cnt)
            cnt = 1
        else:
            cnt+= 1
    answer.append(cnt)

    return answer