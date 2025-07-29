def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if answer.count(numbers[i]+numbers[j]) == 0:
                answer.append(numbers[i]+numbers[j])
            else:
                continue
    answer.sort()
    
    
    return answer