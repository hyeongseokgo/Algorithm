def solution(n, left, right):
    
    
    answer = []
    for i in range(left, right+1):
        point = i%n
        turn = i//n
        if point >= turn+1:
            answer.append(point+1)
        else:
            answer.append(turn+1)
        
    return answer