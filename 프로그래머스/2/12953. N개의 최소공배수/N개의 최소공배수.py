def solution(arr):
    x=2
    while(1):
        check = True
        for i in arr:
            if x % i == 0:
                continue
            else:
                check = False
                break
        if check == True:
            break
        else:
            x+=1
        
    return x