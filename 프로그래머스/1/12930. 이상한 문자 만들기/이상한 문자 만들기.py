def solution(s):
    s = s.split(' ')
    result = []
    for i in s:
        if len(i) == 0:
            result.append(i)
            continue
        temp = ''
        for j in range(len(i)):
            if j%2 == 1:
                temp = temp + i[j].lower()
            else:
                temp = temp + i[j].upper()
        result.append(temp)
    
    result = ' '.join(result)
    
    return result