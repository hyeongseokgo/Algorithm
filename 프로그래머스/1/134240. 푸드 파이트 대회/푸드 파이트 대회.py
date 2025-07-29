def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        answer = answer + str(i)*(food[i]//2)
    answer = answer + '0'
    answer = answer + answer[len(answer)-2::-1]
    
    
    
    
    return answer