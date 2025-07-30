def solution(elements):
    
    number = []
    for i in range(1, len(elements)):
        for j in range(len(elements)):
            su = 0
            if i+j > len(elements):
                su += sum(elements[j:]) + sum(elements[:(i+j)%len(elements)])
            else:
                su += sum(elements[j:j+i])
            number.append(su)
    number = len(set(number))
    return number+1