def solution(k, score):
    answer = []
    result = []
    
    if k <= len(score):
        for i in range(k):
            result.append(score[i])
            result.sort(reverse=True)
            answer.append(result[-1])
    else:
        for i in range(len(score)):
            result.append(score[i])
            result.sort(reverse=True)
            answer.append(result[-1])
    
    
    for i in range(k, len(score)):
        if score[i] > result[-1]:
            result[-1] = score[i]
            result.sort(reverse=True)
            answer.append(result[-1])
        else:
            answer.append(result[-1])
        
    
    
    return answer