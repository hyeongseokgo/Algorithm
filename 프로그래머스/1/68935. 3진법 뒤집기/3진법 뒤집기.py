def solution(n):
    answer = []
    s = 0
    tree= 1
    while n!= 0:
        answer.append(n%3)
        n = n//3
    answer = answer[::-1 ]
    print(answer)
    for i in range(len(answer)):
        
        s += answer[i]*tree
        tree *= 3
    
    return s