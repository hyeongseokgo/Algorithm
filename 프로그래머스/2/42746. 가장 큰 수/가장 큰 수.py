def solution(numbers):
    
    num = [str(i) for i in numbers]
    num.sort(reverse = True, key=lambda x:x*4)
    num = str(int(''.join(num)))
    
    return num