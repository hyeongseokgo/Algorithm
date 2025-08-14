def solution(s, skip, index):
    answer = ''
    
    for i in s:
        point = 1
        time = 0
        while time != index:
            if ord(i)+point > ord('z'):
                temp = chr(ord('a')+(ord(i)+point-ord('a'))%(ord('z')-ord('a')+1))
            else:
                temp = chr(ord(i)+point)
            if temp not in skip:
                time +=1
            point += 1
            
        answer = answer + temp
    print(answer)
    
    
    return answer