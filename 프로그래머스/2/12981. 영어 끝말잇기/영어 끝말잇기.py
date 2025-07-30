def solution(n, words):
    answer = []
    
    check = words[0]
    stop = 0
    for i in range(1, len(words)):
        if check[-1] != words[i][0] or words[:i].count(words[i]) != 0:
            stop += i
            break
        check = words[i]
    
    if stop == 0:
        return [0, 0]
    else:
        return [stop%n+1,stop//n+1]

    return [stop%n,stop//n]