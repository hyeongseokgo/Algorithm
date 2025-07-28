def solution(brown, yellow):
    
    answer = []
    size = brown + yellow
    for i in range(3, size//2):
        if size % i == 0:
            if (i-2)*(size/i-2) == yellow:
                answer.append(size/i)
                answer.append(i)
                break
            
    return answer