def solution(n):
    i = 1
    while n>=i*i:
        if i*i == n:
            return (i+1)*(i+1)
        i+=1
    return -1