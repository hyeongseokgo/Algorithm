def solution(nums):
    
    nums.sort()
    full = sum(nums[-3:])
    sosu = [True] *(full+1)
    sosu[0] = sosu[1] = False
    
    for i in range(1, int(full**0.5)+1):
        if sosu[i]:
            for j in range(i*i, full+1, i):
                sosu[j] = False
    result = []
    def dfs(path, start):
        if len(path) ==3:
            if sosu[sum(path)]:
                result.append(path)
            return
        for i in range(start, len(nums)):
            dfs(path+[nums[i]], i+1)
    dfs([], 0)
    
    

    return len(result)