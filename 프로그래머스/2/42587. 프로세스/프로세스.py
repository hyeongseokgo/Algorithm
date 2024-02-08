def solution(priorities, location):
    num = [x for x in range(len(priorities))]
    cnt = 1
    while(len(num) != 0):
        
        if priorities[0] == max(priorities):
            
            priorities.pop(0)
            a = num.pop(0)
            if a == location:
                break
            cnt += 1
        else:
            priorities.append(priorities.pop(0))
            num.append(num.pop(0))
    
    return cnt