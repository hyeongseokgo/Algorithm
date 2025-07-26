def solution(numbers, target):
    
    answer = 0
    def dfs(index, tsum):
        nonlocal answer
        
        if index == len(numbers):
            if tsum == target:
                answer += 1
            return
        
        dfs(index+1 , tsum+numbers[index])
        dfs(index+1 , tsum-numbers[index])
        return 
        
    dfs(0, 0)
    
    return answer