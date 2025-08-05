def solution(wallet, bill):
    answer = 0
    w_big = max(wallet)
    w_sma = min(wallet)
    
    while 1:
        bill.sort()
        if bill[1] <=w_big and bill[0]<=w_sma:
            break
        bill[1] = bill[1]//2
        answer += 1
            
        
        
    
    
    return answer