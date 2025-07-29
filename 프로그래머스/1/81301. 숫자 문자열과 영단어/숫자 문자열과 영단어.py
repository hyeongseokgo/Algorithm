def solution(s):
    answer = []
    point = 0
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while point < len(s):
        if s[point] >= '0' and s[point] <= '9':
            answer.append(s[point])
            point+= 1
        else:
            if eng.count(s[point:point+3]) == 1:
                for i in range(10):
                    if s[point:point+3] == eng[i]:
                        answer.append(str(i))
                        point+=3
            elif eng.count(s[point:point+4]) == 1:
                for i in range(10):
                    if s[point:point+4] == eng[i]:
                        answer.append(str(i))
                        point+=4
            elif eng.count(s[point:point+5]) == 1:
                for i in range(10):
                    if s[point:point+5] == eng[i]:
                        answer.append(str(i))
                        point+=5
            
        print(answer)
                    
        
    answer = ''.join(answer)
        
    return int(answer)