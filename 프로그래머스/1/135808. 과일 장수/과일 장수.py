def solution(k, m, score):
    result = 0
    score.sort(reverse=True)
    for i in range(m, len(score)+1, m):
        result += score[i-1]*m
    
    return result