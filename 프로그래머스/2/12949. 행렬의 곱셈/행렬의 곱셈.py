def solution(arr1, arr2):
    answer = []
    for i in arr1:
        hang = []
        for j in range(len(arr2[0])):
            plus = 0
            for k in range(len(arr2)):
                plus += arr2[k][j] * i[k]
            hang.append(plus)
        answer.append(hang)
        
        
    
    return answer