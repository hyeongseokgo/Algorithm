def solution(a, b):
    ma = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31,30 ,31]
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = 0
    for i in range(a-1):
        day += ma[i]
    day += b
    
    return week[day%7-1]