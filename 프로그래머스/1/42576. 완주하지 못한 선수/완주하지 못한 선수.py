def solution(participant, completion):
    count = {}
    for i in participant:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for x in completion:
        count[x] -= 1
        if count[x] == 0:
            del count[x]
    answer=list(count.keys())
    return answer[0]