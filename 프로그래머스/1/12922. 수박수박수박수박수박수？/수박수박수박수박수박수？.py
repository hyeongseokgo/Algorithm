def solution(n):
    if n %2 ==0:
        return "수박"*(n//2)
    elif n==1:
        return "수"
    else:
        return "수박"*(n//2)+"수"