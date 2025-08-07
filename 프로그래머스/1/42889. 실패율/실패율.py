def solution(N, stages):
    answer = []
    
    all_n = [0] * (N +1)
    ind = []
    
    for i in range(len(stages)):
        all_n[stages[i]-1] += 1
        
    for i in range(N):
        if sum(all_n[i:]) == 0:
            ind.append([0, i+1])
        else:
            ind.append([all_n[i]/sum(all_n[i:]), i+1])
    
    print(ind)
    ind.sort(reverse=True)
    
    temp = []
    for i in range(N-1):
        temp.append(ind[i][1])
        if ind[i+1][0] != ind[i][0]:
            temp.sort()
            for j in temp:
                answer.append(j)
            temp = []
    if len(temp) == 0:
        answer.append(ind[-1][1])
    else:
        temp.append(ind[-1][1])
        temp.sort()
        for j in temp:
            answer.append(j)
        
    
    return answer