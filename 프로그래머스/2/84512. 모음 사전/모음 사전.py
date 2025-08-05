def solution(word):
    
    moum = ['A', 'E', 'I', 'O','U']
    all_m = []
    def dfs(m):
        if len(m)>5:
            return
        if m:
            all_m.append(m)
        for i in moum:
            dfs(m+i)
    dfs('')
    all_m.sort()
    return all_m.index(word)+1