def solution(strings, n):
    answer = []
    
    
    answer.append(strings[0])
    strings = strings[1:]
    
    for i in range(len(strings)):
        for j in range(len(answer)):
            if strings[i][n] < answer[j][n]:
                answer.insert(j,strings[i])
                break
            elif strings[i][n] == answer[j][n]:
                if strings[i] < answer[j]:
                    answer.insert(j,strings[i])
                    break
                elif j == len(answer)-1 :
                    answer.append(strings[i])
                    
            else:
                if j == len(answer)-1:
                    answer.append(strings[i])
            
                
                
                
                
    
    return answer