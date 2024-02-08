def solution(left, right):
    # 1. 약수 개수가 홀수인경우는 제곱수
    result = 0
    ch = True
    for i in range(left, right+1):
        if i == 1:
            result -= 1
        else:
            for j in range(2, (i//2)+1):
                if j*j == i:
                    ch = False
                    break
            if ch:
                result += i
            else:
                result -= i
            ch = True
    
    return result