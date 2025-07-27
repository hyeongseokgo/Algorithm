def solution(price, money, count):
    allmoney = 0
    for i in range(1, 1+count):
        allmoney+= price*i
        
    if allmoney <= money:
        return 0
    else:
        
        return allmoney-money