def solution(board, h, w):
    answer = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    target = board[h][w]
    for i in range(4):
        if len(board)-1< h+dy[i] or 0>h+dy[i]:
            continue
        if len(board)-1 < w+dx[i]or 0>w+dx[i]:
            continue
        
        if board[h+dy[i]][w+dx[i]] == target:
            answer += 1
    
    
    return answer