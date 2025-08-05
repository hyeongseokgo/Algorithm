def solution(babbling):
    say = ['aya', 'ye', 'ma', 'woo']
    
    answer = 0
    for i in babbling:
        no = ''
        while 1:
            if len(i) == 1:
                break
            elif len(i) == 0:
                answer += 1
                break
            
            if i[:2] in say and i[:2] != no:
                no = i[:2]
                i = i[2:]
                
            elif i[:3] in say and i[:3] != no:
                no = i[:3]
                i = i[3:]
            else:
                break
            
    return answer