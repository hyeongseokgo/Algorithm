def solution(board, moves):
    answer = 0
    doll = []
    
    for i in moves:
        
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                
                if doll and doll[-1] == board[j][i-1]:
                    answer += 2
                    doll.pop()
                else:
                    doll.append(board[j][i-1])
                
                board[j][i-1] = 0
                break
    
    print(doll)
    print(board)
    
    
    
    return answer