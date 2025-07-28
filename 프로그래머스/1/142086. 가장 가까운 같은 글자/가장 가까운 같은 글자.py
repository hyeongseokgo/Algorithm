def solution(s):
    answer = []
    
    alpa = [-1] * 26
    
    for i in range(len(s)):
        temp = ord(s[i])-ord('a')
        answer.append(alpa[temp])
        for j in range(26):
            if alpa[j] != -1:
                alpa[j]+= 1
        alpa[temp] = 1
        
    
    return answer