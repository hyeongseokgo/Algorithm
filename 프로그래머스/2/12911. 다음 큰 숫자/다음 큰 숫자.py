def solution(n):
    
    s = n+1
    bit = bin(n).count('1')
    
    while 1 :
        if bit == bin(s).count('1'):
            break
        else:
            s+= 1 
        
        
    return s