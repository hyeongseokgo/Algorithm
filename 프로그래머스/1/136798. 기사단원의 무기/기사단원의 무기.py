import math as mt
def solution(number, limit, power):
    answer = 0
    yack = [1]
    for i in range(2, number+1):
        count = 2
        for j in range(2, int(mt.sqrt(i))+1):
            if i%j==0:
                if i == j*j:
                    count += 1
                else:
                    count += 2
        if i == 4:
            yack.append(3)
        else:
            yack.append(count)
        
    for i in yack:
        if i > limit:
            answer += power
        else:
            answer += i
    
    
    return answer