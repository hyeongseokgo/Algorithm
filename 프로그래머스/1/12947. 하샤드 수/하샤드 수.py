def solution(x):
    xlist = list(str(x))
    xsum = 0
    for i in xlist:
        xsum += int(i)
    if x % xsum == 0:
        return True
    else:
        return False
    