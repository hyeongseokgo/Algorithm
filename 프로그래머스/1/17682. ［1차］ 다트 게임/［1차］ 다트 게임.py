def solution(dartResult):
    answer = 0
    dart = dartResult
    sdt = ['S', 'D', 'T']
    star = ['*', '#']
    
    num = ''
    before = 0
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num = num + dartResult[i]
        elif dartResult[i] in sdt:
            a = int(num) ** (sdt.index(dartResult[i])+1)
                             
            if i != (len(dartResult)-1):
                if dartResult[i+1] == '*':
                    answer += a*2
                    if before != 0:
                        answer += before
                    before = a*2
                elif dartResult[i+1] == '#':
                    answer -= a
                    before = -a
                else:
                    answer += a
                    before = a
            else:
                answer += a
                before = a
            
            num = ''
        else:
            continue
    
    
    
    
    return answer