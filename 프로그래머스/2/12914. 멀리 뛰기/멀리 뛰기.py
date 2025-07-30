def fac(a):
    result = 1
    for i in range(1, a+1):
        result *= i
    return result

def C(a, b):
    u = 1
    for i in range(b):
        u *=a
        a -= 1
    return u//fac(b)


def solution(n):
    answer = 0
    for i in range(n//2+1):
        answer += C(n-i,i)
    return answer%1234567