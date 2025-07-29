def solution(cards1, cards2, goal):
    
    index1 = 0
    index2 = 0
    
    for i in range(len(goal)):
        if cards1[index1] == goal[i]:
            index1+=1
            if index1 >len(cards1)-1:
                index1 = len(cards1)-1
        elif cards2[index2] == goal[i]:
            index2 += 1
            if index2 >len(cards2)-1:
                index2 = len(cards2)-1
        else:
            return 'No'
        
    return 'Yes'