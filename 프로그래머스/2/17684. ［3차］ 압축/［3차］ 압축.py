

def solution(msg):
    answer = []
    sajon = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    
    index = 0
    while index <= len(msg)-1:
        w = ''
        #현재 입력 찾기
        while index <= len(msg)-1:
            temp = msg[index]
            w = w+temp
            if w in sajon:
                index += 1
                output = sajon.index(w)
            else:
                break
        answer.append(output+1)
        sajon.append(w)
                
        
        
    
    return answer