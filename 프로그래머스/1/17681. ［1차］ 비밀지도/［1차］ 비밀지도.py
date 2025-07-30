def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        two = bin(arr1[i]|arr2[i])[2:].zfill(n)
        two = two.replace('0', ' ')
        two = two.replace('1', '#')
        answer.append(''.join(two))
        
    
    
    return answer