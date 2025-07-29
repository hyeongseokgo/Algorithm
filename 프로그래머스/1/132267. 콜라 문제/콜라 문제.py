def solution(a, b, n):
    answer = 0
    sev = 0
    while n >= a:
        sev = n//a
        sev *= b
        n = sev+n%a
        answer += sev
    return answer