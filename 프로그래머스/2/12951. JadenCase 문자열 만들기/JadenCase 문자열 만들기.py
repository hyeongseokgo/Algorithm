def solution(s):
    
    s_split=s.split(' ')
    answer = []
    for i in s_split:
        if len(i) == 0:
            answer.append(i)
            continue
        if i[0] >='0' and i[0] <='9':
            answer.append(i.lower())
        else:
            temp = i[0].upper()
            temp += i[1:].lower()
            answer.append(temp)
    return ' '.join(answer)