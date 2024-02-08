def solution(x, y):
    
    a = [0,0,0,0,0,0,0,0,0,0]
    b = [0,0,0,0,0,0,0,0,0,0] 
    for i in range(10):
        if x.count(str(i)) > y.count(str(i)):
            a[i] = y.count(str(i))
        else:
            a[i] = x.count(str(i))
    answer = []
    for j in range(9, -1, -1):
        if a[j] != 0:
            answer.append(str(j)*a[j])
    
    if not answer:
        answer.append('-1')
    if (len(answer) == 1) & (answer[0].find('0') >=0):
        answer[0] = '0'
        
    answer = ''.join(answer)
    answer
        
    return answer