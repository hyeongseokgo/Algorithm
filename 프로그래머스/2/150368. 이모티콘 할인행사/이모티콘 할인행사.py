all_emo = []

def dfs(num, path):
    if len(path)>=num:
        all_emo.append(path)
        return 
    
    for i in [10, 20, 30, 40]:
        dfs(num, path+ [i])
    

def solution(users, emoticons):
    answer = [0,0]
    
    dfs(len(emoticons), [])
    
    for i in all_emo:
        gaip = 0
        all_m = 0
        for j in users:
            summoney = 0
            for k in range(len(emoticons)):
                if j[0]<= i[k]:
                    summoney += emoticons[k]-emoticons[k]*(i[k]/100)
                
            if summoney >= j[1]:
                gaip += 1
            else:
                all_m += summoney
                
        if answer[0] < gaip:
            answer = [gaip, int(all_m)]
        elif answer[0] == gaip:
            if answer[1] <= all_m:
                answer = [gaip, int(all_m)]
                
    
    return answer