def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        max_index = land[i-1].index(max(land[i-1]))
        two_big = max([land[i-1][x] for x in range(4) if x != max_index])
        for j in range(4):
            if max_index == j:
                land[i][j] += two_big
            else:
                land[i][j] += max(land[i-1])
    
    return max(land[-1])