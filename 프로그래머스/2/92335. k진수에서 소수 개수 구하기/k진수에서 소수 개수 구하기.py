def sosu(num, k):
    a = ''
    while num >= k:
        a =  str(num%k) + a
        num = num//k
    a = str(num) + a
    return a

def solution(n, k):
    answer = 0
    
    temp = sosu(n, k)
    temp = temp.split('0')
    for i in temp:
        check = True
        if len(i) == 0:
            continue
        a = int(i)
        if a == 1:
            continue
        elif a == 2:
            answer += 1
        else:
            for j in range(2, int(a**0.5) +1):
                if a%j == 0:
                    check = False
                    break
            if check == True:
                answer += 1
        
            
    return answer