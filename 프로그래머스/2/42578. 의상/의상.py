def solution(clothes):
    
    clo_type =[]
    clo_num = []
    
    
    for i in clothes:
        if i[1] in clo_type:
            clo_num[clo_type.index(i[1])] += 1
        else:
            clo_type.append(i[1])
            clo_num.append(1)
    
    answer = 1
    for i in clo_num:
        answer *= (i+1)
    return answer-1