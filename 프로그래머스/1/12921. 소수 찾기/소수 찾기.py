def solution(n):
    
    #에라토스 테네스의 체
    check = [True] * (n+1)
    check[0] = False
    check[1] = False
    
    for i in range(1, int(n**0.5)+1):
        if check[i] == True:
            for j in range(i*i, n+1, i):
                check[j] = False
    
    
    return sum(check)