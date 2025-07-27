def solution(s):
    s = list(s)
    if len(s)!=4 and len(s)!=6:
        return False
    for i in s:
        if i>'9':
            return False
    return True