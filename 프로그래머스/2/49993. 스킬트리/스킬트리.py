def solution(skill, skill_trees):
    answer = 0
    check = True
    
    for i in skill_trees:
        before = -2
        for j in range(len(skill)):
            if skill[j] in i:
                a = i.index(skill[j])
                if before < a and before != -1:
                    before = a
                    continue
                else:
                    check = False
                    break
            else:
                before = -1
                
        if check:
            answer +=1
        check = True
            
        
    return answer