def solution(files):
    answer = []
    name = []
    
    for i in range(len(files)):
        idx = i
        i = files[i]
        start = -1
        end = -1
        for j in range(len(i)):
            if i[j].isdigit():
                if start == -1:
                    start = j
                    end = j
                else:
                    end += 1
            elif start != -1:
                break
        
        name.append([i[:start].lower(), int(i[start:end+1]),idx, i])
    
    name.sort()
    for i in name:
        answer.append(i[3])
    
    return answer