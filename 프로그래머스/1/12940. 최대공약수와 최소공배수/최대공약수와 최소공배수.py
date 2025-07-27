def solution(n, m):
    answer = []
    sm = 1
    bi = 1
    con = False
    for i in range(1, min(n, m)+1):
        if n%i==0 and m%i==0:
            sm = i
        
        if (max(n, m)*i)%min(n, m)==0 and con==False:
            bi = max(n, m)*i
            con = True
    
        
    
    
    return [sm, bi]